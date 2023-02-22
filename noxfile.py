"""nox-poetry configuration file."""

# FIXME: Handle poetry install when shoal is recursively required...

from calcipy.noxfile import build_check, build_dist, tests  # noqa: F401
