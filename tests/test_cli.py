import pytest
from click.testing import CliRunner
from dtac_cli import cli


@pytest.fixture
def runner():
    return CliRunner()


