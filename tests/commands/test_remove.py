from .CommandTest import CommandTest

class RemoveCommandTest(CommandTest):

    def test_remove(self):
        before1 = 'file1{t1}{t2}{t3}.txt'
        before2 = 'file2{t1}.txt'
        before3 = 'file3{t3}.txt'
        after1 = 'file1{t3}.txt'
        after2 = 'file2.txt'
        after3 = 'file3{t3}.txt'
        self.run_command_test(
            command = f'remove --verbose t1,t2 {before1} {before2} {before3}',
            touch = [before1, before2, before3],
            assert_exist = [after1, after2, after3],
            assert_not_exist = [before1, before2],
            output = f'{before1} -> {after1}\n' \
                + f'{before2} -> {after2}\n\n' \
                + '2 files renamed.\n',
        )

    def test_debug(self):
        before = 'file{t1}.txt'
        after = 'file.txt'
        self.run_command_test(
            command = f'remove --debug t1 {before}',
            touch = [before],
            assert_exist = [before],
            assert_not_exist = [after],
        )
