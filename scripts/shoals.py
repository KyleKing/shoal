"""shoal demo.

```sh
# See all tangs
poetry run python scripts/shoals.py --task-help

# Run the Tang
poetry run python scripts/shoals.py test-jq

# Optionally pass path arguments through 'argv'
poetry run python scripts/shoals.py test-jq scripts/shoals.py README.md
```

"""

import json
import subprocess  # noqa: S404  # nosec

from beartype import beartype
from beartype.typing import List

from shoal import capture_shell, register_fun, shell, shoalling, get_logger

logger = get_logger()


@beartype
def test_jq(argv: List[str]) -> None:
    """Example Tang to run jq."""
    logger.info(f'Running with argv={argv}')

    jq = 'jq'
    try:
        capture_shell(f'{jq} --help')
    except subprocess.CalledProcessError:
        jq = 'gojq'  # Fallback to jq
        capture_shell(f'{jq} --help')

    # Then show the output with or without color
    logger.info('With captured shell output:')
    data = {value: value * 1_000 for value in range(3)}
    capture_shell(f"echo '{json.dumps(data)}' | {jq}", printer=print)
    logger.info('With ANSII Color codes:')
    shell(f"echo '{json.dumps(data)}' | {jq}")


# Assemble each Tang
register_fun(test_jq)

shoalling()
