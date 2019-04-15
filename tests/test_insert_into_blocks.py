import unittest
import sys
sys.path.append('.')
from main import insert_into_blocks


class InsertIntoBlocksTestCase(unittest.TestCase):
	def setUp(self):
		self.coordinates = {'x': '1', 'y': '1', 'z': 1}

	def test_row_does_not_exist(self):
		blocks = {}
		insert_into_blocks(blocks, True, self.coordinates)
		self.assertTrue(blocks[self.coordinates['x']][self.coordinates['y']][self.coordinates['z']])


if __name__ == '__main__':
    unittest.main()