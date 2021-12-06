from click.testing import CliRunner
from pathlib import Path
from tag.cli import cli
import os
import unittest

class CommandTest(unittest.TestCase):

    def run_command_test(self, command, touch, assert_exist = [], assert_not_exist = [], output = '', debug = False):
        runner = CliRunner()
        with runner.isolated_filesystem():
            for path in touch:
                parent = os.path.split(path)[0]
                if parent:
                    os.makedirs(parent, exist_ok=True)
                Path(path).touch()
            if debug:
                print('\nCommand: ' + command)
                print('Before:')
                print(os.system('tree -a'))
            result = runner.invoke(cli, command)
            if debug:
                print('After:')
                print(os.system('tree -a'))
            self.assertEqual(result.exit_code, 0, result.output)
            cwd = os.getcwd()
            self.assertEqual(result.output, output.replace('@cwd', cwd))
            for path in assert_exist:
                self.assertTrue(Path(path).is_file(), f'file should exist: {path}')
            for path in assert_not_exist:
                self.assertFalse(Path(path).is_file(), f'file should not exist: {path}')
