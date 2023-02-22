import shlex
from subprocess import CalledProcessError  # nosec

import pytest

from shoal.shell import capture_shell


def test_capture_shell_gibberish():
    with pytest.raises(CalledProcessError):
        capture_shell('gibberish')


def test_capture_shell(fake_process):
    process = 'git branch'
    expected = 'fake output'
    fake_process.register(shlex.split(process), stdout=[expected, ''])

    result = capture_shell(process)

    assert result == expected + '\n\n'
