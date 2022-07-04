#!/usr/bin/env python3
"""Tests for CLI scripts"""

# Core Library modules

# Third party modules
from click.testing import CliRunner

# First party modules
from gitwatch import gitwatch_cli


def test_author() -> None:
    """Test function to assert correct author name."""
    runner = CliRunner()
    result = runner.invoke(gitwatch_cli.author)
    assert result.exit_code == 0
    assert result.output == "Author name: Stephen R A King\n"


def test_author_verbose() -> None:
    """Test function to assert correct verbose author name."""
    runner = CliRunner()
    result = runner.invoke(gitwatch_cli.author, ["--verbose"])
    assert result.exit_code == 0
    assert (
        result.output == "Author name: Stephen R A King\n"
        "Author eMail: stephen.ra.king@gmail.com\n"
    )


def test_author_help() -> None:
    """Test function to assert correct author help text."""
    runner = CliRunner()
    result = runner.invoke(gitwatch_cli.author, ["--help"])
    assert result.exit_code == 0
    assert "  Display Author Name" in result.output
