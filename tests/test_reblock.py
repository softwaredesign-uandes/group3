import unittest
import sys
import mock
from decimal import *

sys.path.append('.')
from main import reblock

class GetMaxCoordsOfModelTestCase(unittest.TestCase):
    def test_reblock(self):
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

        units = {'copper': '%'}
        block_model = reblock(block_model,100,100,100,units)
        total_weight = 72360 + 72360 + Decimal('72240.00781') + Decimal('71670.01563') + Decimal('71550.01563')

        total_cooper = Decimal('71550.01563')*Decimal(71550)/100 +Decimal('71670.01563')*Decimal(71670)/100 + Decimal('72240.00781')*Decimal(72240)/100 + Decimal(72360)*Decimal(72360)/100 +Decimal(72360)*Decimal(72360)/100
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

        self.assertEqual(block_model,expected_model)



if __name__ == '__main__':
    unittest.main()
