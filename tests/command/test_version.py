from .CommandTest import CommandTest
import tag

expected_output = f'''tag {tag.__version__}
License {tag.__license__}: {tag.__license_long__}
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by {tag.__author__}.
'''

class VersionCommandTest(CommandTest):

    def test_version_command(self):
        self.run_command_test(
            command = 'version',
            output = expected_output,
        )

    def test_version_option(self):
        self.run_command_test(
            command = '--version',
            output = expected_output,
        )
