"""Start the command line program."""

from . import __pkg_name__, __version__


def start() -> None:
    """Run the customized Invoke Program."""
    from calcipy.cli import start_program  # noqa: PLC0415
    from calcipy.tasks import all_tasks  # noqa: PLC0415
    start_program(__pkg_name__, __version__, all_tasks)
