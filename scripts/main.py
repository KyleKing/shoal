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

from shoal import Tang, capture_shell, register, shell, shoalling


@beartype
def test_jq(_argv: List[str]) -> None:
    # Example error handling
    jq = 'jq'
    try:
        capture_shell(f'{jq} --help')
    except subprocess.CalledProcessError:
        jq = 'gojq'  # Fallback to jq
        capture_shell(f'{jq} --help')

    # Then show the output with or without color
    print('With captured shell output:\n')
    data = {value: value * 1_000 for value in range(3)}
    capture_shell(f"echo '{json.dumps(data)}' | {jq}", printer=print)
    print('\nWith ANSII Color codes:\n')
    shell(f"echo '{json.dumps(data)}' | {jq}")


# Assemble each Tang
register(Tang(target='test-jq', description='Example calling jq', fun=test_jq))

shoalling()
