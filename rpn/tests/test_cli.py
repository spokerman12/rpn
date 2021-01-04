#
# test_file_cli.py: Unit tests for cli function.
#


import pytest
from ..cli import launch_cli, interactive_mode


def test_base():
    assert True


def test_launch_cli_help_01(capsys):
    with pytest.raises(SystemExit) as e:
        launch_cli(["rpn", "help"])
        captured = capsys.readouterr()[0]
        assert "Reverse Polish Notation Calculator - Documentation" in captured
        assert e.type == SystemExit
        assert e.value.code == 0


def test_launch_cli_help_02(capsys):
    with pytest.raises(SystemExit) as e:
        launch_cli(["rpn", "-help"])
        captured = capsys.readouterr()[0]
        assert "Reverse Polish Notation Calculator - Documentation" in captured
        assert e.type == SystemExit
        assert e.value.code == 0


def test_launch_cli_help_03(capsys):
    with pytest.raises(SystemExit) as e:
        launch_cli(["rpn", "--help"])
        captured = capsys.readouterr()[0]
        assert "Reverse Polish Notation Calculator - Documentation" in captured
        assert e.type == SystemExit
        assert e.value.code == 0


def test_launch_cli_help_05(capsys):
    with pytest.raises(SystemExit) as e:
        launch_cli(["rpn", "-h"])
        captured = capsys.readouterr()[0]
        assert "Reverse Polish Notation Calculator - Documentation" in captured
        assert e.type == SystemExit
        assert e.value.code == 0


def test_launch_cli_help_06(capsys):
    with pytest.raises(SystemExit) as e:
        launch_cli(["rpn", "--h"])
        captured = capsys.readouterr()[0]
        assert "Reverse Polish Notation Calculator - Documentation" in captured
        assert e.type == SystemExit
        assert e.value.code == 0
