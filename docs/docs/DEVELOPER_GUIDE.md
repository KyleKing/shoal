# Developer Notes

## Local Development

```sh
git clone https://github.com/kyleking/shoal.git
cd shoal
poetry install

# See the available tasks
poetry run doit list

# Run the default task list (lint, auto-format, test coverage, etc.)
poetry run doit --continue

# Make code changes and run specific tasks as needed:
poetry run doit run test
```

## Publishing

For testing, create an account on [TestPyPi](https://test.pypi.org/legacy/). Replace `...` with the API token generated on TestPyPi or PyPi respectively

```sh
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry config pypi-token.testpypi ...

poetry run doit run publish_test_pypi
# If you didn't configure a token, you will need to provide your username and password to publish
```

To publish to the real PyPi

```sh
poetry config pypi-token.pypi ...
poetry run doit run publish

# For a full release, triple check the default tasks, increment the version, rebuild documentation (twice), and publish!
poetry run doit run --continue
poetry run doit run cl_bump lock document deploy_docs publish

# For pre-releases use cl_bump_pre
poetry run doit run cl_bump_pre -p rc
poetry run doit run lock document deploy_docs publish
```

## Current Status

<!-- {cts} COVERAGE -->
| File                         |   Statements |   Missing |   Excluded | Coverage   |
|------------------------------|--------------|-----------|------------|------------|
| `shoal/__init__.py`          |            7 |         0 |          0 | 100.0%     |
| `shoal/_private/__init__.py` |            0 |         0 |          0 | 100.0%     |
| `shoal/_private/cli.py`      |           12 |        12 |          0 | 0.0%       |
| `shoal/ling.py`              |           19 |        19 |         13 | 0.0%       |
| `shoal/shell.py`             |           31 |        31 |          0 | 0.0%       |
| `shoal/tang.py`              |           11 |        11 |          0 | 0.0%       |
| `shoal/tangs.py`             |           18 |        18 |          0 | 0.0%       |
| **Totals**                   |           98 |        91 |         13 | 7.1%       |

Generated on: 2023-02-06
<!-- {cte} -->