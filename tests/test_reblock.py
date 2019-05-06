import unittest
import sys
from decimal import *

sys.path.append('.')
from main import reblock
from main import get_max_coords_of_model

class GetMaxCoordsOfModelTestCase(unittest.TestCase):
    def setUp(self):
        self.units = {'copper': '%'}
        self.block_model_filled = {'0':
                           {'0':
                                {'0':
                                     {'weight': '100', 'mineral': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'mineral': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'mineral': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'mineral': {'cu': '50'}}},
                            '1':
                                {'0':
                                     {'weight': '100', 'mineral': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'mineral': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'mineral': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'mineral': {'cu': '50'}}},
                            '2':
                                {'0':
                                     {'weight': '100', 'mineral': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'mineral': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'mineral': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'mineral': {'cu': '50'}}},
                            '3':
                                {'0':
                                     {'weight': '100', 'mineral': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'mineral': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'mineral': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'mineral': {'cu': '50'}}}
                            },
                       '1':
                           {'0':
                                {'0':
                                     {'weight': '100', 'mineral': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'mineral': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'mineral': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'mineral': {'cu': '50'}}},
                            '1':
                                {'0':
                                     {'weight': '100', 'mineral': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'mineral': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'mineral': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'mineral': {'cu': '50'}}},
                            '2':
                                {'0':
                                     {'weight': '100', 'mineral': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'mineral': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'mineral': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'mineral': {'cu': '50'}}},
                            '3':
                                {'0':
                                     {'weight': '100', 'mineral': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'mineral': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'mineral': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'mineral': {'cu': '50'}}}
                            },
                       '2':
                           {'0':
                                {'0':
                                     {'weight': '100', 'mineral': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'mineral': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'mineral': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'mineral': {'cu': '50'}}},
                            '1':
                                {'0':
                                     {'weight': '100', 'mineral': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'mineral': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'mineral': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'mineral': {'cu': '50'}}},
                            '2':
                                {'0':
                                     {'weight': '100', 'mineral': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'mineral': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'mineral': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'mineral': {'cu': '50'}}},
                            '3':
                                {'0':
                                     {'weight': '100', 'mineral': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'mineral': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'mineral': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'mineral': {'cu': '50'}}}
                            },
                       '3':
                           {'0':
                                {'0':
                                     {'weight': '100', 'mineral': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'mineral': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'mineral': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'mineral': {'cu': '50'}}},
                            '1':
                                {'0':
                                     {'weight': '100', 'mineral': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'mineral': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'mineral': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'mineral': {'cu': '50'}}},
                            '2':
                                {'0':
                                     {'weight': '100', 'mineral': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'mineral': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'mineral': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'mineral': {'cu': '50'}}},
                            '3':
                                {'0':
                                     {'weight': '100', 'mineral': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'mineral': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'mineral': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'mineral': {'cu': '50'}}}
                            }
                       }
        self.block_model_with_air = {
            '0': {
                '0': {
                    '0': {
                        'minerals': {
                            'copper': '10'
                        },
                        'weight': '71550.01563'
                    }
                }
            },
            '14': {
                '17': {
                    '19': {
                        'minerals': {
                            'copper': '30'
                        },
                        'weight': '71670.01563'
                    }
                }
            },
            '15': {
                '17': {
                    '10': {
                        'minerals': {
                            'copper': '50'
                        },
                        'weight': '72240.00781'
                    }
                }
            },
            '16': {
                '18': {
                    '10': {
                        'minerals': {
                            'copper': '70'
                        },
                        'weight': '72360'
                    }
                }
            },
            '17': {
                '17': {
                    '10': {
                        'minerals': {
                            'copper': '0'
                        },
                        'weight': '72360'
                    }
                }
            }
        }

    def test_mid_reblock_factor_and_all_blocks_filled(self):
        block_model = {'0':
                           {'0':
                                {'0':
                                     {'weight': '100', 'minerals': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'minerals': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'minerals': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'minerals': {'cu': '50'}}},
                            '1':
                                {'0':
                                     {'weight': '100', 'minerals': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'minerals': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'minerals': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'minerals': {'cu': '50'}}},
                            '2':
                                {'0':
                                     {'weight': '100', 'minerals': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'minerals': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'minerals': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'minerals': {'cu': '50'}}},
                            '3':
                                {'0':
                                     {'weight': '100', 'minerals': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'minerals': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'minerals': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'minerals': {'cu': '50'}}}
                            },
                       '1':
                           {'0':
                                {'0':
                                     {'weight': '100', 'minerals': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'minerals': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'minerals': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'minerals': {'cu': '50'}}},
                            '1':
                                {'0':
                                     {'weight': '100', 'minerals': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'minerals': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'minerals': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'minerals': {'cu': '50'}}},
                            '2':
                                {'0':
                                     {'weight': '100', 'minerals': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'minerals': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'minerals': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'minerals': {'cu': '50'}}},
                            '3':
                                {'0':
                                     {'weight': '100', 'minerals': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'minerals': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'minerals': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'minerals': {'cu': '50'}}}
                            },
                       '2':
                           {'0':
                                {'0':
                                     {'weight': '100', 'minerals': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'minerals': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'minerals': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'minerals': {'cu': '50'}}},
                            '1':
                                {'0':
                                     {'weight': '100', 'minerals': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'minerals': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'minerals': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'minerals': {'cu': '50'}}},
                            '2':
                                {'0':
                                     {'weight': '100', 'minerals': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'minerals': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'minerals': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'minerals': {'cu': '50'}}},
                            '3':
                                {'0':
                                     {'weight': '100', 'minerals': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'minerals': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'minerals': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'minerals': {'cu': '50'}}}
                            },
                       '3':
                           {'0':
                                {'0':
                                     {'weight': '100', 'minerals': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'minerals': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'minerals': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'minerals': {'cu': '50'}}},
                            '1':
                                {'0':
                                     {'weight': '100', 'minerals': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'minerals': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'minerals': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'minerals': {'cu': '50'}}},
                            '2':
                                {'0':
                                     {'weight': '100', 'minerals': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'minerals': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'minerals': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'minerals': {'cu': '50'}}},
                            '3':
                                {'0':
                                     {'weight': '100', 'minerals': {'cu': '10'}},
                                 '1':
                                     {'weight': '500', 'minerals': {'cu': '50'}},
                                 '2':
                                     {'weight': '200', 'minerals': {'cu': '30'}},
                                 '3':
                                     {'weight': '500', 'minerals': {'cu': '50'}}}
                            }
                       }

        units = {'cu': '%'}
        reblocked_model = reblock(block_model, 2, 2, 2, units)
        weight_per_block = str(100*4 + 500*4)
        percent_per_block = str((10*4 + 50*4)/Decimal(8))
        expected_reblocked_model = {'0':
                                        {'0':
                                             {'0':
                                                  {'weight': weight_per_block, 'minerals': {'cu': percent_per_block}},
                                              '1':
                                                  {'weight': weight_per_block, 'minerals': {'cu': percent_per_block}}},
                                         '1':
                                             {'0':
                                                  {'weight': weight_per_block, 'minerals': {'cu': percent_per_block}},
                                              '1':
                                                  {'weight': weight_per_block, 'minerals': {'cu': percent_per_block}}}
                                         },
                                    '1':
                                        {'0':
                                             {'0':
                                                  {'weight': weight_per_block, 'mineral': {'cu': percent_per_block}},
                                              '1':
                                                  {'weight': weight_per_block, 'mineral': {'cu': percent_per_block}}},
                                         '1':
                                             {'0':
                                                  {'weight': weight_per_block, 'mineral': {'cu': percent_per_block}},
                                              '1':
                                                  {'weight': weight_per_block, 'mineral': {'cu': percent_per_block}}}
                                         }}

        self.assertEqual(reblocked_model, expected_reblocked_model)

    def test_small_reblock_factor_and_filled_model(self):
        block_model = self.block_model_filled
        expected_block_model = block_model
        reblocked_model = reblock(block_model,1,1,1,self.units)
        self.assertEqual(expected_block_model,reblocked_model)

    def test_small_reblock_factor_and_model_with_air(self):
        block_model = self.block_model_with_air
        reblocked_model = reblock(block_model,1,1,1,self.units)
        max_x, max_y, max_z = get_max_coords_of_model(block_model)
        default_block = {'weight': '0', 'minerals': {} }
        available_z = range(0, max_z + 1)
        z_blocks = dict(map(lambda x: (x, default_block), available_z))
        available_y = range(0, max_y + 1)
        y_blocks = dict(map(lambda x: (x, z_blocks), available_y))
        available_x = range(0, max_x + 1)
        expected_reblocked_model = dict(map(lambda x: (x, y_blocks), available_x))
        expected_reblocked_model.update(block_model)
        self.assertEqual(expected_reblocked_model,reblocked_model)



    def test_reblock_weight(self):
        reblocked_model = reblock(self.block_model_with_air, 1, 1, 1, self.units)
        expected_total_weight = 72360 + 72360 + Decimal('72240.00781') + Decimal('71670.01563') + Decimal('71550.01563')
        total_weight = reblocked_model['0']['0']['0']['weight']
        self.assertEqual(expected_total_weight, total_weight)

    def test_reblock_with_ppm_units(self):
        units = {'copper': 'ppm'}
        reblocked_model = reblock(self.block_model_with_air, 1, 1, 1, units)
        expected_total_copper = str((Decimal('10') + Decimal('30') + Decimal('50') + Decimal('70') + Decimal('0')) / 5)
        total_copper = reblocked_model['0']['0']['0']['minerals']['copper']
        self.assertEqual(expected_total_copper, total_copper)

    def test_reblock_void_model(self):
        block_model = {}
        reblocked_model = reblock(block_model, 5, 10, 2, {})
        expected_reblocked_model = {}
        self.assertEqual(expected_reblocked_model, reblocked_model)

    def test_reblock_by_unitary_factor(self):
        reblocked_model = reblock(self.block_model_with_air, 1, 1, 1, self.units)
        expected_reblocked_model = self.block_model_with_air
        self.assertEqual(expected_reblocked_model, reblocked_model)

    def test_reblock_with_percentage_units(self):
        units = {'copper': '%'}
        reblocked_model = reblock(self.block_model_with_air, 1, 1, 1, units)
        expected_total_copper = str((Decimal('10') + Decimal('30') + Decimal('50') + Decimal('70') + Decimal('0')) / 5)
        total_copper = reblocked_model['0']['0']['0']['minerals']['copper']

        self.assertEqual(expected_total_copper, total_copper)

    def test_small_reblock_factor_and_air_model(self):
        block_model = self.block_model_with_air
        expected_reblocked_model = block_model
        reblocked_model = reblock(block_model,1,1,1,self.units)
        self.assertEqual(expected_reblocked_model,reblocked_model)

        # max_x, max_y, max_z = get_max_coords_of_model(block_model)
        # default_block = {'weight': '0', 'minerals': {} }
        # available_z = range(0, max_z + 1)
        # z_blocks = dict(map(lambda x: (x, default_block), available_z))
        # available_y = range(0, max_y + 1)
        # y_blocks = dict(map(lambda x: (x, z_blocks), available_y))
        # available_x = range(0, max_x + 1)
        # blocks = dict(map(lambda x: (x, y_blocks), available_x))
        # blocks.update(block_model)



    def test_high_reblock_factor_and_air_model(self):
        block_model = {
            '0': {
                '0': {
                    '0': {
                        'minerals': {
                            'copper': '71550'
                        },
                        'weight': '71550.01563'
                    }
                }
            },
            '14': {
                '17': {
                    '19': {
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
                '18': {
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

        units = {'copper': '%', 'au': '%'}
        block_model = reblock(block_model, 100, 100, 100, units)
        total_weight = 72360 + 72360 + Decimal('72240.00781') + Decimal('71670.01563') + Decimal('71550.01563')

        total_cooper = (Decimal(71550) + Decimal(71670) + Decimal(72240) + Decimal(72360) + Decimal(72360))/5
        expected_model = {
            0: {
                0: {
                    0: {
                        'minerals': {
                            'copper': total_cooper
                        },
                        'weight': total_weight

                    }
                }
            }
        }

        self.assertEqual(block_model, expected_model)


if __name__ == '__main__':
    unittest.main()
