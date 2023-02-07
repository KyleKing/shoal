"""Log."""

import logging
from functools import partial

from beartype import beartype
from beartype.typing import Any, Callable
from pydantic import BaseModel

_DEF_LEVEL = logging.ERROR


@beartype
def _log(message, *, _log_level: int, _this_level: int, **kwargs) -> None:
    """Default log function."""
    if _this_level >= _log_level:
        print(message)
        if kwargs:
            raise NotImplementedError('kwargs are not yet implemented')


class _LogSingleton(BaseModel):
    """Store pointer to log function."""

    log: Callable[[Any], None]


_LOG_SINGLETON = _LogSingleton(log=partial(_log, _log_level=_DEF_LEVEL))


class _Logger:

    @beartype
    def debug(self, message, **kwargs) -> None:
        _LOG_SINGLETON.log(message, _this_level=logging.DEBUG, **kwargs)

    @beartype
    def info(self, message, **kwargs) -> None:
        _LOG_SINGLETON.log(message, _this_level=logging.INFO, **kwargs)

    @beartype
    def warning(self, message, **kwargs) -> None:
        _LOG_SINGLETON.log(message, _this_level=logging.WARNING, **kwargs)

    @beartype
    def error(self, message, **kwargs) -> None:
        _LOG_SINGLETON.log(message, _this_level=logging.ERROR, **kwargs)

    @beartype
    def exception(self, message, **kwargs) -> None:
        _LOG_SINGLETON.log(message, _this_level=logging.EXCEPTION, **kwargs)


@beartype
def configure_logger(log_level: int = _DEF_LEVEL) -> None:
    """Configure global logger."""
    _LOG_SINGLETON.log = partial(_log, _log_level=log_level)


@beartype
def get_logger() -> _Logger:
    """Retrieve global logger."""
    return _Logger()
