from .CommandTest import CommandTest

class ListCommandTest(CommandTest):

    def test_list_default_path(self):
        file1 = './file1{t1}{t2}{t3}.txt'
        file2 = './file2{t1}.txt'
        file3 = './file3.txt'
        file4 = './.file4{t4}.txt'
        self.run_command_test(
            command = f'list',
            touch = [file1, file2, file3, file4],
            assert_exist = [file1, file2, file3, file4],
            output = 't1\nt2\nt3\n',
        )

    def test_list_with_path(self):
        file1 = 'dir/file1{t1}{t2}{t3}.txt'
        file2 = 'dir/file2{t1}.txt'
        file3 = 'dir/file3.txt'
        self.run_command_test(
            command = f'list dir',
            touch = [file1, file2, file3],
            output = 't1\nt2\nt3\n',
        )

    def test_list_with_count(self):
        file1 = 'dir/file1{t1}{t2}{t3}.txt'
        file2 = 'dir/file2{t1}.txt'
        file3 = 'dir/file3{t1}{t2}.txt'
        self.run_command_test(
            command = f'list --count dir',
            touch = [file1, file2, file3],
            output = 't1: 3\nt2: 2\nt3: 1\n',
        )

    def test_list_null(self):
        file = 'dir/file1{t1}{t2}.txt'
        self.run_command_test(
            command = f'list --null dir',
            touch = [file],
            output = 't1\0t2',
        )

    def test_list_all(self):
        file1 = './file1{t1}.txt'
        file2 = './.file2{t2}.txt'
        self.run_command_test(
            command = f'list --all',
            touch = [file1, file2],
            output = 't1\nt2\n',
        )

    def test_list_recursive(self):
        file1 = './file1{t1}.txt'
        file2 = './dir/file2{t2}.txt'
        self.run_command_test(
            command = f'list --recursive',
            touch = [file1, file2],
            output = 't1\nt2\n',
        )
