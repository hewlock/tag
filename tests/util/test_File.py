from tag.util.File import File
from unittest.mock import patch
import os
import unittest

MOCK_PATH = '/mock/path'

def abspath(filename):
    return os.path.join(MOCK_PATH, filename)

class FileTest(unittest.TestCase):

    @patch('os.path.abspath', new=abspath)
    def test_absolute_path(self):
        file = File('filename{a}{c}{b}.txt')
        self.assertEqual(file.absolute_path, MOCK_PATH + '/filename{a}{b}{c}.txt')

    @patch('os.path.abspath', new=abspath)
    def test_tags(self):
        file = File('filename{a}{c}{b}.txt')
        self.assertSetEqual(file.tags, {'a', 'b', 'c'})
