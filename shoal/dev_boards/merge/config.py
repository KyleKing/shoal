"""Merge Config."""

from functools import lru_cache

from beartype import beartype
from beartype.typing import Dict
from pydantic import BaseModel


class Config(BaseModel):
    """Merge Config."""

    search_kwargs: Dict[str, str]


@lru_cache(maxsize=1)
@beartype
def get_config() -> Config:
    """Load the user configuration data."""
    return Config(
        search_kwargs={'author': '@me', 'review': 'approved', 'state': 'open'},
    )
