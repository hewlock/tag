from .CommandTest import CommandTest

class IndexCommandTest(CommandTest):

    def test_index(self):
        file1 = './file1{t1}{t2}.txt'
        file2 = './file2{t1}.txt'
        file3 = './file3.txt'
        file4 = './.file4{t3}.txt'
        self.run_command_test(
            command = f'index . index',
            touch = [file1, file2, file3, file4],
            assert_exist = [
                file1,
                file2,
                file3,
                file4,
                f'./index/t1/{file1}',
                f'./index/t1/{file2}',
                f'./index/t2/{file1}',
            ],
        )

    def test_index_all(self):
        file1 = './file1{t1}.txt'
        file2 = './.file2{t1}.txt'
        self.run_command_test(
            command = f'index --all . index',
            touch = [file1, file2],
            assert_exist = [
                f'./index/t1/{file1}',
                f'./index/t1/{file2}',
            ],
        )

    def test_index_debug(self):
        file1 = './file1{t1}{t2}.txt'
        file2 = './file2{t1}.txt'
        self.run_command_test(
            command = f'index --debug . index',
            touch = [file1, file2],
            assert_not_exist = [
                f'./index/t1/{file1}',
                f'./index/t1/{file2}',
                f'./index/t2/{file1}',
            ],
        )

    def test_index_recursive(self):
        file1 = './file1{t1}.txt'
        file2 = 'dir/file2{t1}.txt'
        self.run_command_test(
            command = f'index --recursive . index',
            touch = [file1, file2],
            assert_exist = [
                f'./index/t1/{file1}',
                './index/t1/file2{t1}.txt',
            ],
        )

    def test_index_name_collision(self):
        file = 'file{t1}.txt'
        file1 = f'dir1/{file}'
        file2 = f'dir2/{file}'
        self.run_command_test(
            command = f'index --recursive . index',
            touch = [file1, file2],
            assert_exist = [
                './index/t1/file{t1}-dir1.txt',
                './index/t1/file{t1}-dir2.txt',
            ],
        )


    def test_index_tree(self):
        file = './file{t1}{t2}.txt'
        self.run_command_test(
            command = f'index --tree . index',
            touch = [file],
            assert_exist = [
                f'./index/t1/{file}',
                f'./index/t1/t2/{file}',
                f'./index/t2/{file}',
                f'./index/t2//t1/{file}',
            ],
        )

    def test_index_verbose(self):
        file1 = 'file1{t1}{t2}.txt'
        file2 = 'file2{t1}.txt'
        self.run_command_test(
            command = f'index --verbose . index',
            touch = [file1, file2],
            output = f'''index/t1/{file1} -> @cwd/{file1}
index/t1/{file2} -> @cwd/{file2}
index/t2/{file1} -> @cwd/{file1}

3 files indexed.
'''
        )
