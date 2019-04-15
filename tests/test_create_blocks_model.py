import unittest
import sys
sys.path.append('.')
from main import create_blocks_model, load_file


class CreateBlocksModelTestCase(unittest.TestCase):
	def setUp(self):
		self.coordinates = {'x': 1, 'y': 2, 'z': 3}
		self.ores = {'copper': 7}
		self.weight = 6
		self.block_as_list_of_parameters = load_file('tests/zuck_small.txt')
		self.result = {
			'13': {
				'17': {
					'10': {
						'minerals': {
							'copper': '71550'
						},
						'weight': '71550.01563'
					}
				}
			},
			'14': {
				'17': {
					'10': {
						'minerals': {
							'copper': '71670'
						},
						'weight': '71670.01563'
					}
				}
			},
			'15': {
				'17': {
					'10': {
						'minerals': {
							'copper': '72240'
						},
						'weight': '72240.00781'
					}
				}
			},
			'16': {
				'17': {
					'10': {
						'minerals': {
							'copper': '72360'
						},
						'weight': '72360'
					}
				}
			},
			'17': {
				'17': {
					'10': {
						'minerals': {
							'copper': '72360'
						},
						'weight': '72360'
					}
				}
			}
		}

	def test_creates_blocks_correctly(self):
		blocks = create_blocks_model(self.block_as_list_of_parameters, self.coordinates, self.ores, self.weight)
		self.assertEqual(blocks, self.result)


if __name__ == '__main__':
    unittest.main()