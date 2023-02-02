"""Tang (task model).

```sh
  _
><_>
```

"""

from beartype.typing import Callable, List
from pydantic import BaseModel, Field


class Tang(BaseModel):
    """A singular task (named after the Tang fish).

    The naming and logic derives from Makefiles:

    ```sh
    .PHONY target
    target: prerequisites
    <TAB> recipe
    ```

    https://www.gnu.org/software/make/manual/html_node/Introduction.html

    """

    target: str
    """Name of the task."""

    recipe: List[Callable]
    """Steps in the task."""

    description: str = ''
    """Optional help text."""

    prerequisities: List[str] = Field(default_factory=list)
    """Optional task and/or file prerequisities."""

    phony: bool = False
    """Set to True if the `target` should *not* be included in the file preqreuisites.

    By default, assumes that the target name is associated with the matching file.

    https://stackoverflow.com/a/2145605/3219667

    """
