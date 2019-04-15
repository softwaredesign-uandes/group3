import unittest
import sys
sys.path.append('.')
from main import load_file


class LoadFileTestCase(unittest.TestCase):
	def setUp(self):
		self.file_name = 'tests/zuck_small.txt'
		self.false_file_name = 'tests/false.txt'
		self.result = [
			['0', '13', '17', '10', '64395.01407', '95076.276', '71550.01563', '71550'],
			['1', '14', '17', '10', '64503.01407', '148258.148', '71670.01563', '71670'],
			['2', '15', '17', '10', '65016.00703', '223559.0336', '72240.00781', '72240'],
			['3', '16', '17', '10', '65124', '372664.0976', '72360', '72360'],
			['4', '17', '17', '10', '65124', '531604.448', '72360', '72360']
		]

	def test_file_loads_correctly(self):
		self.assertEqual(load_file(self.file_name), self.result)

	def test_file_does_not_exists(self):
		with self.assertRaises(FileNotFoundError):
			load_file(self.false_file_name)


if __name__ == '__main__':
    unittest.main()