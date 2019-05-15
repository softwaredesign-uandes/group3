import unittest
import sys
sys.path.append('.')
from main import get_block_mineral_weight, get_block_weight

class GetBlockWeightTestCase(unittest.TestCase):

    def test_get_block_mineral_weight_with_percentage_units(self):

        units = {'au': '%','cu':'%'}
        block = {'weight': 100, 'minerals': {'au': 50,'cu': 10}}
        expected_mineral_weight = 60.0
        block_mineral_weight = get_block_mineral_weight(block,units)
        self.assertEqual(block_mineral_weight,expected_mineral_weight)

    def test_get_block_mineral_weight_with_ppm_units(self):
        units = {'au': 'ppm', 'cu': 'ppm'}
        block = {'weight': 1000000, 'minerals': {'au': 50, 'cu': 10}}
        expected_mineral_weight = 50 + 10
        block_mineral_weight = get_block_mineral_weight(block, units)
        self.assertEqual(block_mineral_weight, expected_mineral_weight)

    def test_get_block_mineral_weight_with_mixed_units(self):
        units = {'au': '%', 'cu': 'ppm'}
        block = {'weight': 1000000, 'minerals': {'au': 50, 'cu': 10}}
        expected_mineral_weight = 500000 + 10
        block_mineral_weight = get_block_mineral_weight(block, units)
        self.assertEqual(block_mineral_weight, expected_mineral_weight)

    def test_get_correct_block_weight(self):
        block = {'weight': 500, 'minerals': {'au': 50, 'cu': 10}}
        expected_block_weight = 500
        block_weight = get_block_weight(block)
        self.assertEqual(block_weight, expected_block_weight)

if __name__ == '__main__':
    unittest.main()
