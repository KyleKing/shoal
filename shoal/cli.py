"""Extend Invoke for Calcipy."""

import logging
import os
import sys
from functools import wraps
from pathlib import Path
from types import ModuleType

from beartype import beartype
from beartype.typing import Any, Callable, Dict, List
from invoke import Collection, Config, Context, Program, Task
from invoke import task as invoke_task  # noqa: TID251
from invoke.config import merge_dicts
from pydantic import BaseModel, Field, PositiveInt

from .invoke_helpers import use_pty
from .log import configure_logger, get_logger

logger = get_logger()


class GlobalTaskOptions(BaseModel):
    """Global Task Options."""

    working_dir: Path = Field(default_factory=Path.cwd)
    """Working directory for the program to use globally."""

    file_args: List[Path] = Field(default_factory=list)
    """List of Paths to modify."""

    verbose: PositiveInt = Field(default=1, lte=3)
    """Verbosity level."""


class _ShoalProgram(Program):  # type: ignore[misc]
    """Customized version of Invoke's `Program`."""

    def print_help(self) -> None:
        """Extend print_help with shoal-specific global configuration.

        https://github.com/pyinvoke/invoke/blob/0bcee75e4a26ad33b13831719c00340ca12af2f0/invoke/program.py#L657-L667

        """
        super().print_help()
        print('Global Task Options:')  # noqa: T201
        print('')  # noqa: T201
        self.print_columns([
            ('working_dir', 'Set the cwd for the program. Example: "../run --working-dir .. lint test"'),
            ('*file_args', 'List of Paths available globally to all tasks. Will resolve paths with working_dir'),
            ('verbose', 'Globally configure logger verbosity (-vvv for most verbose)'),
        ])
        print('')  # noqa: T201


class ShoalConfig(Config):  # type: ignore[misc]
    """Opinionated Config with better defaults."""

    @staticmethod
    def global_defaults() -> Dict:  # type: ignore[type-arg]
        """Override the global defaults."""
        invoke_defaults = Config.global_defaults()
        shoal_defaults = {
            'run': {
                'asynchronous': False,  # PLANNED: When can this be True?
                'echo': True,
                'echo_format': '\033[2;3;37mRunning: {command}\033[0m',
                'pty': use_pty(),
            },
        }
        return merge_dicts(invoke_defaults, shoal_defaults)  # type: ignore[no-any-return]


@beartype
def start_program(pkg_name: str, pkg_version: str, module: ModuleType) -> None:
    """Run the customized Invoke Program.

    FYI: recommendation is to extend the `core_args` method, but this won't parse positional arguments:
    https://docs.pyinvoke.org/en/stable/concepts/library.html#modifying-core-parser-arguments

    """
    # Manipulate 'sys.argv' to hide arguments that invoke can't parse
    _gto = GlobalTaskOptions()
    sys_argv: List[str] = sys.argv[:1]
    last_argv = ''
    for argv in sys.argv[1:]:
        if not last_argv.startswith('-') and Path(argv).is_file():
            _gto.file_args.append(Path(argv))
        elif argv in {'-v', '-vv', '-vvv', '--verbose'}:
            _gto.verbose = argv.count('v')
        elif last_argv in {'--working-dir'}:
            _gto.working_dir = Path(argv).resolve()
        elif argv not in {'--working-dir'}:
            sys_argv.append(argv)
        last_argv = argv
    _gto.file_args = [
        _f if _f.is_absolute() else Path.cwd() / _f
        for _f in _gto.file_args
    ]
    sys.argv = sys_argv

    class _ShoalConfig(ShoalConfig):

        gto: GlobalTaskOptions = _gto

    _ShoalProgram(
        name=pkg_name,
        version=pkg_version,
        namespace=Collection.from_module(module),
        config_class=_ShoalConfig,
    ).run()


@beartype
def task(*task_args: Any, **task_kwargs: Any) -> Callable[[Any], Task]:
    """Wrapper to accept arguments for an invoke task."""
    @beartype
    def wrapper(func: Any) -> Task:  # noqa: ANN001
        """Wraps the decorated task."""
        @invoke_task(*task_args, **task_kwargs)  # type: ignore[misc]
        @beartype
        @wraps(func)
        def inner(ctx: Context, *args: Any, **kwargs: Any) -> Task:
            """Wrap the task with settings configured in `gto` for working_dir and logging."""
            try:
                ctx.config.gto
            except AttributeError:
                ctx.config.gto = GlobalTaskOptions()

            os.chdir(ctx.config.gto.working_dir)

            verbose = ctx.config.gto.verbose
            log_lookup = {3: logging.NOTSET, 2: logging.DEBUG, 1: logging.INFO, 0: logging.WARNING}
            raw_log_level = log_lookup.get(verbose)
            configure_logger(log_level=logging.ERROR if raw_log_level is None else raw_log_level)

            summary = func.__doc__.split('\n')[0]
            logger.text(f'Running {func.__name__}', is_header=True, summary=summary)
            logger.text_debug('With task arguments', args=args, kwargs=kwargs)

            result = func(ctx, *args, **kwargs)

            logger.text_debug(f'Completed {func.__name__}', result=result)
            return result
        return inner
    return wrapper
