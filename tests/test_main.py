import unittest
import sys
sys.path.append('.')
from main import check_row


class CheckRowTestCase(unittest.TestCase):
	def test_key_does_not_exists(self):
		dictionary = {}
		check_row(dictionary, '1')
		self.assertTrue('1' in dictionary.keys())

	def test_key_exists(self):
		dictionary = {'1': True}
		check_row(dictionary, '1')
		self.assertTrue(dictionary['1'])


if __name__ == '__main__':
    unittest.main()