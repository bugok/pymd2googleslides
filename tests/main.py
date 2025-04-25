#!/usr/bin/env python3

import testslide
from click.testing import CliRunner
from main import cli


class MainTest(testslide.TestCase):
    def test_sanity(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        self.assertEquals(0, result.exit_code)
