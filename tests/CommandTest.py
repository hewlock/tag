from click.testing import CliRunner
from pathlib import Path
from tag.cli import cli
import unittest

class CommandTest(unittest.TestCase):

    def run_command_test(self, command, touch, assert_exist, assert_not_exist, output = ''):
        runner = CliRunner()
        with runner.isolated_filesystem():
            for path in touch:
                Path(path).touch()
            result = runner.invoke(cli, command)
            self.assertEqual(result.exit_code, 0, result.output)
            self.assertEqual(result.output, output)
            for path in assert_exist:
                self.assertTrue(Path(path).is_file(), f'file should exist: {path}')
            for path in assert_not_exist:
                self.assertFalse(Path(path).is_file(), f'file should not exist: {path}')
