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

from shoal.log import get_logger
from shoal.shell import capture_shell, run_shell

logger = get_logger()


@beartype
def test_jq() -> None:
    """Example to run jq."""
    jq = 'gojq'
    try:
        capture_shell(f'{jq} --help')
    except subprocess.CalledProcessError:
        jq = 'jq'  # Fallback to jq
        capture_shell(f'{jq} --help')

    # Then show the output with or without color
    logger.info('With captured shell output:')
    data = {value: value * 1_000 for value in range(3)}
    capture_shell(f"echo '{json.dumps(data)}' | {jq}", printer=print)
    logger.info('With ANSII Color codes:')
    run_shell(f"echo '{json.dumps(data)}' | {jq}")


test_jq()
