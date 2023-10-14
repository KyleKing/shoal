"""Configure CLI 'tasks'."""

from calcipy.cli import task
from invoke.context import Context

from ..merge.app import MergeApp


@task()  # type: ignore[misc]
def merge(_ctx: Context) -> None:
    """Merge Task."""
    MergeApp().run()
