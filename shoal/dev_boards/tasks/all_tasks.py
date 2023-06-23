"""Configure CLI 'tasks'."""

from beartype import beartype
from invoke.context import Context
from invoke.tasks import task

from ..merge.app import MergeApp


@task()
@beartype
def merge(_ctx: Context) -> None:
    """Merge Task."""
    MergeApp().run()
