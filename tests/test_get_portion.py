import unittest
import sys
import mock


sys.path.append('.')
from main import get_portion


class GetPortionTestCase(unittest.TestCase):

    def test_get_portion_with_percentage(self):
        block_weight = 100
        mineral_weight = 10
        unit = '%'
        portion = get_portion(block_weight,mineral_weight,unit)
        expected_portion = block_weight*mineral_weight/100
        self.assertEqual(portion,expected_portion)

    def test_get_portion_with_ppm(self):
        block_weight = 1000000
        mineral_weight = 10
        unit = 'ppm'
        portion = get_portion(block_weight, mineral_weight, unit)
        expected_portion = 10
        self.assertEqual(portion, expected_portion)

if __name__ == '__main__':
    unittest.main()
