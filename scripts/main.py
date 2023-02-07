"""shoal demo.

```sh
# See all tangs
poetry run python scripts/main.py --task-help

# Run the Tang
poetry run python scripts/main.py test-jq

# Optionally pass path arguments through 'argv'
poetry run python scripts/main.py test-jq scripts/main.py README.md
```

"""

import json
import subprocess  # noqa: S404  # nosec

from beartype import beartype
from beartype.typing import List

from shoal.ling import shoalling
from shoal.shell import capture_shell, shell
from shoal.tang import Tang
from shoal.tangs import register


@beartype
def test_jq(_argv: List[str]) -> None:
    # Check the executable because aliases won't work
    jq = 'jq'
    try:
        capture_shell(f'{jq} --help')
    except subprocess.CalledProcessError:
        jq = 'gojq'  # Fallback to jq
        capture_shell(f'{jq} --help')

    # Then show the output with or without color
    data = {value: value * 1_000 for value in range(3)}
    capture_shell(f"echo '{json.dumps(data)}' | gojq", printer=print)
    print('\nWith ANSII Color codes:\n')
    shell(f"echo '{json.dumps(data)}' | gojq")


@beartype
def tested_jq(argv: List[str]) -> None:
    print(f'jq was tested for {argv}')


# Assemble each Tang
register(Tang(target='test-jq', description='Example calling jq', recipe=[test_jq, tested_jq]))

shoalling()
