import unittest
import os
from my-activity.utils import get_file_size

class UtilsTestCase(unittest.TestCase):
    def test_get_file_size(self):
        with open('test.txt', 'w') as f:
            f.write('test')
        self.assertEqual(get_file_size('test.txt'), 4)
        os.remove('test.txt')

if __name__ == '__main__':
    unittest.main()
