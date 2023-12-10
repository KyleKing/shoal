"""Start the command line program."""

from beartype import beartype

from . import __pkg_name__, __version__
from .cli import start_program


@beartype
def start() -> None:  # pragma: no cover
    """Run the customized Invoke Program."""
    from .tasks import all_tasks  # noqa: PLC0415
    start_program(__pkg_name__, __version__, all_tasks)
