"""Check that all imports work as expected.

Primarily checking that:

1. No optional dependencies are required

FIXME: Replace with programmatic imports? Maybe explicit imports to check backward compatibility of public API?
    https://stackoverflow.com/questions/34855071/importing-all-functions-from-a-package-from-import

"""

from pprint import pprint

from shoal import shell, capture_shell, register_fun, shoalling, configure_logger, get_logger  # noqa: F401

pprint(locals())  # noqa: T003
