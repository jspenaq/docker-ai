import pytest
from click.testing import CliRunner
from docker_ai.cli import main
import sys
from unittest.mock import patch


def test_command_line_query():
    runner = CliRunner()
    # the input data for sys.argv
    result = runner.invoke(main, ["list all containers"])
    assert result.exit_code == 0  # Exit code 0 means success
    assert "Query received: list all containers" in result.output


def test_standard_input_query():
    runner = CliRunner()
    # the input data for sys.stdin
    result = runner.invoke(main, input="list all containers\n")
    assert result.exit_code == 0
    assert "Query received: list all containers" in result.output


def test_no_query_provided():
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 1
    assert "No query provided." in result.output


def test_help_flag():
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output
    assert "Options:" in result.output
    assert "--quiet" in result.output  # Check presence of options defined in main
    assert "-q" in result.output


def test_empty_query_after_stdin():
    runner = CliRunner()
    result = runner.invoke(main, input="\n")
    assert result.exit_code == 1
    assert "No query provided." in result.output


def test_quiet_option():
    runner = CliRunner()
    result = runner.invoke(main, ["list all containers", "--quiet"])
    assert result.exit_code == 0
    assert "Query received: list all containers" in result.output
    assert "Quiet mode: True" in result.output


def test_short_quiet_option():
    runner = CliRunner()
    result = runner.invoke(main, ["list all containers", "-q"])
    assert result.exit_code == 0
    assert "Query received: list all containers" in result.output
    assert "Quiet mode: True" in result.output
