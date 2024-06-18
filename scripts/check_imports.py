"""Check that all imports work as expected in the built package."""

from pprint import pprint

from shoal.scripts import start

pprint(locals())  # noqa: T203
