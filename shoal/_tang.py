"""Tang (task model).

```sh
  _
><_>
```

"""

from beartype import beartype
from beartype.typing import Callable, List
from pydantic import BaseModel


class Tang(BaseModel):
    """A singular task (named after the Tang fish).

    The inner naming and logic derives from Makefiles: https://www.gnu.org/software/make/manual/html_node/Introduction.html

    ```sh
    .PHONY target
    target: prerequisites
    <TAB> recipe
    ```

    """

    target: str
    """Name of the task."""

    fun: Callable[[List[str]], None]
    """Tang callable."""

    description: str = ''
    """Optional help text."""

    # > PLANNED: Add support for these additional arguments

    # prerequisites: List[str] = Field(default_factory=list)
    # """Optional task and/or file prerequisites."""

    # phony: bool = False
    # """Set to True if the `target` should *not* be included in the file preqreuisites.
    #
    # By default, assumes that the target name is associated with the matching file.
    #
    # https://stackoverflow.com/a/2145605/3219667
    #
    # """

    @beartype
    def run(self, args: List[str]) -> None:
        self.fun(args)
