from .CommandTest import CommandTest
from tag import version

class VersionCommandTest(CommandTest):

    def test_version_command(self):
        self.run_command_test(
            command = 'version',
            output = f'{version}\n',
        )

    def test_version_option(self):
        self.run_command_test(
            command = '--version',
            output = f'{version}\n',
        )
