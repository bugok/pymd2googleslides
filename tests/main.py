#!/usr/bin/env python3

import testslide
from click.testing import CliRunner
from pymd2googleslides.main import cli


class MainTest(testslide.TestCase):
    def test_sanity(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        self.assertEqual(0, result.exit_code)
