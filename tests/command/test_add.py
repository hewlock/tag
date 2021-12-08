from .CommandTest import CommandTest

class AddCommandTest(CommandTest):

    def test_add_tag_to_file(self):
        before = 'file.txt'
        after = 'file{t1}.txt'
        self.run_command_test(
            command = f'add t1 {before}',
            touch = [before],
            assert_exist = [after],
            assert_not_exist = [before],
        )

    def test_add_tags_to_file(self):
        before = 'file.txt'
        after = 'file{t1}{t2}.txt'
        self.run_command_test(
            command = f'add t2,t1 {before}',
            touch = [before],
            assert_exist = [after],
            assert_not_exist = [before],
        )

    def test_add_tags_to_files(self):
        before1 = 'file1.txt'
        before2 = 'file2.txt'
        after1 = 'file1{t1}{t2}.txt'
        after2 = 'file2{t1}{t2}.txt'
        self.run_command_test(
            command = f'add t2,t1 {before1} {before2}',
            touch = [before1, before2],
            assert_exist = [after1, after2],
            assert_not_exist = [before1, before2],
        )

    def test_add_tags_to_tagged_files(self):
        before1 = 'file1{t3}{t1}.txt'
        before2 = 'file2{t3}{t2}.txt'
        after1 = 'file1{t1}{t2}{t3}.txt'
        after2 = 'file2{t1}{t2}{t3}.txt'
        self.run_command_test(
            command = f'add t2,t1 {before1} {before2}',
            touch = [before1, before2],
            assert_exist = [after1, after2],
            assert_not_exist = [before1, before2],
        )

    def test_debug(self):
        before = 'file.txt'
        after = 'file{t1}.txt'
        self.run_command_test(
            command = f'add --debug t1 {before}',
            touch = [before],
            assert_exist = [before],
            assert_not_exist = [after],
        )

    def test_verbose_singular(self):
        before = 'file.txt'
        after = 'file{t1}.txt'
        self.run_command_test(
            command = f'add --verbose t1 {before}',
            touch = [before],
            assert_exist = [after],
            assert_not_exist = [before],
            output = f'{before} -> {after}\n\n' \
                + '1 file renamed.\n',
        )

    def test_verbose_skips_unchanged(self):
        before1 = 'file1.txt'
        before2 = 'file2{t1}.txt'
        after1 = 'file1{t1}.txt'
        after2 = 'file2{t1}.txt'
        self.run_command_test(
            command = f'add --verbose t1 {before1} {before2}',
            touch = [before1, before2],
            assert_exist = [after1, after2],
            assert_not_exist = [before1],
            output = f'{before1} -> {after1}\n\n' \
                + '1 file renamed.\n',
        )

    def test_verbose_plural(self):
        before1 = 'file1.txt'
        before2 = 'file2.txt'
        after1 = 'file1{t1}.txt'
        after2 = 'file2{t1}.txt'
        self.run_command_test(
            command = f'add --verbose t1 {before1} {before2}',
            touch = [before1, before2],
            assert_exist = [after1, after2],
            assert_not_exist = [before1, before2],
            output = f'{before1} -> {after1}\n' \
                + f'{before2} -> {after2}\n\n' \
                + '2 files renamed.\n',
        )
