"""Configure CLI 'tasks'."""

from beartype import beartype
from invoke.context import Context
from invoke.tasks import task


@task()
@beartype
def merge(_ctx: Context) -> None:
    """Merge Task."""
    ...
