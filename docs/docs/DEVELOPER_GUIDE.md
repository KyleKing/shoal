# Developer Notes

## Local Development

```sh
git clone https://github.com/kyleking/shoal.git
cd shoal
poetry install --sync
poetry run calcipy-pack pack.install-extras

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
| File                                   |   Statements |   Missing |   Excluded | Coverage   |
|----------------------------------------|--------------|-----------|------------|------------|
| `shoal/__init__.py`                    |            4 |         0 |          0 | 100.0%     |
| `shoal/_runtime_type_check_setup.py`   |           13 |         0 |         28 | 100.0%     |
| `shoal/dev_boards/__init__.py`         |            2 |         2 |          0 | 0.0%       |
| `shoal/dev_boards/cli.py`              |            5 |         5 |         13 | 0.0%       |
| `shoal/dev_boards/merge/__init__.py`   |            0 |         0 |          0 | 100.0%     |
| `shoal/dev_boards/merge/app.py`        |           75 |        75 |          0 | 0.0%       |
| `shoal/dev_boards/merge/config.py`     |           10 |        10 |          0 | 0.0%       |
| `shoal/dev_boards/merge/gh_wrapper.py` |           59 |        59 |          0 | 0.0%       |
| `shoal/dev_boards/scripts.py`          |            3 |         3 |          5 | 0.0%       |
| `shoal/dev_boards/tasks/__init__.py`   |            0 |         0 |          0 | 100.0%     |
| `shoal/dev_boards/tasks/all_tasks.py`  |            6 |         6 |          0 | 0.0%       |
| `shoal/scripts.py`                     |            5 |         5 |          0 | 0.0%       |
| **Totals**                             |          182 |       165 |         46 | 7.7%       |

Generated on: 2024-06-18
<!-- {cte} -->
