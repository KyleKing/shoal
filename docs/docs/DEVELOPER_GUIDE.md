# Developer Notes

## Local Development

```sh
git clone https://github.com/kyleking/shoal.git
cd shoal
poetry install --sync

# See the available tasks
poetry run calcipy
# Or use a local 'run' file (so that 'calcipy' can be extended)
./run

# Run the default task list (lint, auto-format, test coverage, etc.)
./run main

# Make code changes and run specific tasks as needed:
./run lint.fix test
```

## Publishing

For testing, create an account on [TestPyPi](https://test.pypi.org/legacy/). Replace `...` with the API token generated on TestPyPi or PyPi respectively

```sh
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry config pypi-token.testpypi ...

./run main pack.publish --to-test-pypi
# If you didn't configure a token, you will need to provide your username and password to publish
```

To publish to the real PyPi

```sh
poetry config pypi-token.pypi ...
./run release

# Or for a pre-release
./run release --suffix=rc
```

## Current Status

<!-- {cts} COVERAGE -->
| File                      |   Statements |   Missing |   Excluded | Coverage   |
|---------------------------|--------------|-----------|------------|------------|
| `shoal/__init__.py`       |            7 |         0 |          0 | 100.0%     |
| `shoal/can_skip.py`       |           19 |         3 |          0 | 84.2%      |
| `shoal/cli.py`            |           80 |        80 |          0 | 0.0%       |
| `shoal/invoke_helpers.py` |           20 |        20 |          0 | 0.0%       |
| `shoal/log.py`            |           85 |        20 |          0 | 76.5%      |
| `shoal/pretty_process.py` |           59 |        59 |          0 | 0.0%       |
| `shoal/shell.py`          |           34 |         5 |          0 | 85.3%      |
| **Totals**                |          304 |       187 |          0 | 38.5%      |

Generated on: 2023-02-21
<!-- {cte} -->
