"""shoal."""

__version__ = '1.0.0rc0'
__pkg_name__ = 'shoal'

# ====== Above is the recommended code from calcipy_template and may be updated on new releases ======

from os import environ
from warnings import filterwarnings

from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

if not environ.get('BEARTYPE_SHOW_WARNINGS'):
    # FYI: https://github.com/beartype/beartype#are-we-on-the-worst-timeline
    filterwarnings('ignore', category=BeartypeDecorHintPep585DeprecationWarning)
