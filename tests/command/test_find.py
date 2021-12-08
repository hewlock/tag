from .CommandTest import CommandTest

class FindCommandTest(CommandTest):

    def test_find_default_path(self):
        file1 = './file1{t1}{t2}{t3}.txt'
        file2 = './file2{t1}.txt'
        file3 = './file3.txt'
        file4 = './.file4{t1}.txt'
        self.run_command_test(
            command = f'find t1',
            touch = [file1, file2, file3, file4],
            assert_exist = [file1, file2, file3, file4],
            output = f'{file1}\n{file2}\n',
        )

    def test_find_with_path(self):
        file1 = 'dir/file1{t1}{t2}{t3}.txt'
        file2 = 'dir/file2{t1}.txt'
        file3 = 'dir/file3.txt'
        self.run_command_test(
            command = f'find t1 dir',
            touch = [file1, file2, file3],
            output = f'{file1}\n{file2}\n',
        )

    def test_find_null(self):
        file1 = './file1{t1}{t2}{t3}.txt'
        file2 = './file2{t1}.txt'
        self.run_command_test(
            command = f'find --null t1',
            touch = [file1, file2],
            output = f'{file1}\0{file2}',
        )

    def test_find_all(self):
        file1 = './.dir/.file3{t1}.txt'
        file2 = './.file2{t1}.txt'
        file3 = './file1{t1}.txt'
        self.run_command_test(
            command = f'find --all t1',
            touch = [file1, file2, file3],
            output = f'{file2}\n{file3}\n',
        )

    def test_find_recursive(self):
        file1 = './dir/file3{t1}.txt'
        file2 = './file1{t1}.txt'
        file3 = './file2{t1}.txt'
        self.run_command_test(
            command = f'find --recursive t1',
            touch = [file1, file2, file3],
            output = f'{file1}\n{file2}\n{file3}\n',
        )

    def test_find_all_recursive(self):
        file1 = './.dir/.file3{t1}.txt'
        file2 = './.file2{t1}.txt'
        file3 = './file1{t1}.txt'
        self.run_command_test(
            command = f'find --all --recursive t1',
            touch = [file1, file2, file3],
            output = f'{file1}\n{file2}\n{file3}\n',
        )

    def test_find_tree(self):
        file1 = 'file{t1}.txt'
        file2 = 'dir1/file{t1}.txt'
        file3 = 'dir2/file{t1}.txt'
        self.run_command_test(
            command = f'find --tree --recursive t1',
            touch = [file1, file2, file3],
            output = '''.
├── dir1
│   └── file{t1}.txt
├── dir2
│   └── file{t1}.txt
└── file{t1}.txt
''',
        )
