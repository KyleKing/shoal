"""Configure CLI 'tasks'."""

from calcipy.cli import task
from invoke.context import Context

from shoal.dev_boards.merge.app import MergeApp


@task()
def merge(_ctx: Context) -> None:
    """Merge Task."""
    MergeApp().run()
