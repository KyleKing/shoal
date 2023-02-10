"""shoal."""

from warnings import filterwarnings

from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

__version__ = '0.2.0'
__pkg_name__ = 'shoal'

# ====== Above is the recommended code from calcipy_template and may be updated on new releases ======

# FYI: https://github.com/beartype/beartype#are-we-on-the-worst-timeline
filterwarnings('ignore', category=BeartypeDecorHintPep585DeprecationWarning)

from ._shoalling import shoalling  # noqa: E402,E408
from ._log import configure_logger, get_logger  # noqa: E402,E408
from ._shell import capture_shell, shell  # noqa: E402,E408
from ._tangs import register_fun  # noqa: E402,E408
