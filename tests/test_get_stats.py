import unittest
import sys
sys.path.append('.')
import main
from main import get_stats, get_block_mineral_weight, get_block_weight


class GetStatsTestCase(unittest.TestCase):

    def test_a(self):

        blocks = {'0': {'0': {'0': {'weight':'10','minerals':{'au':'100'}}
                            },
                        '1': {'0': {'weight':'20', 'minerals':{'au':'50'}}}},
                  '1': {'0': {'0': {'weight':'30', 'minerals':{'au':'50'}}},
                       '1': {'0': {'weight':'40.5', 'minerals':{'au':'100'}}}}}
        units = {'au': '%'}
        expected_stats =  dict(blocks_number=4,
                                total_weight=100.5,
                                total_mineral_weight=10+10+15+40.5,
                                air_blocks_number =0)
        stats = get_stats(blocks,units)
        self.assertEqual(stats,expected_stats)

if __name__ == '__main__':
    unittest.main()
