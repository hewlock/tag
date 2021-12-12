from .CommandTest import CommandTest
import tag

class VersionCommandTest(CommandTest):

    def test_version_command(self):
        self.run_command_test(
            command = 'version',
            output = f'{tag.__version__}\n',
        )

    def test_version_option(self):
        self.run_command_test(
            command = '--version',
            output = f'{tag.__version__}\n',
        )
