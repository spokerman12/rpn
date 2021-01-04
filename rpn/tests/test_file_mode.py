#
# test_file_mode.py: Unit tests for file mode
# 					 These tests tend to fail
# 					 if you print additional dialog.

import pytest
import os

from ..cli import launch_cli


def test_file_mode_00(capsys):
    launch_cli(["rpn", "--read", "./rpn/tests/test_file"])
    captured = capsys.readouterr()[0]
    assert "4\n0x80000\n" in str(captured)
