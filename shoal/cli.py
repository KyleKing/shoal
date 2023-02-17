"""Extend Invoke for Calcipy."""

import sys
from pathlib import Path

from beartype import beartype
from beartype.typing import List
from invoke import Collection, Config, Program
from pydantic import BaseModel


class GlobalTaskOptions(BaseModel):
    """Global Task Options."""

    file_args: List[Path]
    verbose: int

class _ShoalProgram(Program):
    """Customized version of Invoke's `Program`."""

    def print_help(self) -> None:
        """Extend print_help with shoal-specific global configuration.

        https://github.com/pyinvoke/invoke/blob/0bcee75e4a26ad33b13831719c00340ca12af2f0/invoke/program.py#L657-L667

        """
        super().print_help()
        print('Global Task Options:')  # noqa: T201
        print('')  # noqa: T201
        self.print_columns([
            ('*file_args', 'List of Paths available globally to all tasks'),
            ('verbose', 'Globally configure logger verbosity (-vvv for most verbose)'),
        ])
        print('')  # noqa: T201


@beartype
def start_program(pkg_name: str, pkg_version: str, module) -> None:
    """Run the customized Invoke Program.

    FYI: recommendation is to extend the `core_args` method, but this won't parse positional arguments:
    https://docs.pyinvoke.org/en/stable/concepts/library.html#modifying-core-parser-arguments

    """
    # Manipulate 'sys.argv' to hide arguments that invoke can't parse
    file_argv: List[Path] = []
    verbose_argv: int = 0
    sys_argv: List[str] = []
    last_argv = ''
    for argv in sys.argv:
        if not last_argv.startswith('-') and Path(argv).is_file():
            file_argv.append(Path(argv))
        elif argv in {'-v', '-vv', '-vvv', '--verbose'}:
            verbose_argv = argv.count('v')
        else:
            sys_argv.append(argv)
        last_argv = argv
    sys.argv = sys_argv

    class ShoalConfig(Config):

        gto: GlobalTaskOptions = GlobalTaskOptions(file_args=file_argv, verbose=verbose_argv)

    _ShoalProgram(
        name=pkg_name,
        version=pkg_version,
        namespace=Collection.from_module(module),
        config_class=ShoalConfig,
    ).run()
