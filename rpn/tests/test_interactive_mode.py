#
# test_interactive_mode.py: Unit tests for interactive mode
#


import pytest
from ..cli import interactive_mode


def test_interactive_mode_exit(capsys):
    with pytest.raises(SystemExit) as e:
        interactive_mode("exit")
        assert e.type == SystemExit
        assert e.value.code == 0


def test_interactive_mode_help(capsys):
    interactive_mode("help")
    captured = capsys.readouterr()[0]
    assert "Reverse Polish Notation Calculator - Documentation" in captured


def test_interactive_mode_calc_00(capsys):
    interactive_mode("2 + 2")
    captured = capsys.readouterr()[0]
    assert "Error" in captured


def test_interactive_mode_calc_01(capsys):
    interactive_mode("2 2 +")
    captured = capsys.readouterr()[0].split("\n")
    assert "4" == captured[len(captured) - 2]


def test_interactive_mode_calc_02(capsys):
    interactive_mode("2 12 + --hex")
    captured = capsys.readouterr()[0].split("\n")
    assert "0xe" == captured[len(captured) - 2]


def test_interactive_mode_calc_03(capsys):
    interactive_mode("2 --hex 12 +")
    captured = capsys.readouterr()[0].split("\n")
    assert "0xe" == captured[len(captured) - 2]
