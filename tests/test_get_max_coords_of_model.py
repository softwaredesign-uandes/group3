import unittest
import sys


sys.path.append('.')
from main import get_max_coords_of_model


class GetMaxCoordsOfModelTestCase(unittest.TestCase):

    def test_max_coords_of_a_void_model(self):
        block_model={}
        x_result, y_result, z_result = -1,-1,-1
        x_max, y_max, z_max = get_max_coords_of_model(block_model)
        self.assertEqual(x_max, x_result)
        self.assertEqual(y_max, y_result)
        self.assertEqual(z_max, z_result)


    def test_max_coords_of_model(self):
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

            x_result, y_result, z_result = 17,18,19
            x_max, y_max, z_max = get_max_coords_of_model(block_model)
            self.assertEqual(x_max,x_result)
            self.assertEqual(y_max,y_result)
            self.assertEqual(z_max,z_result)



if __name__ == '__main__':
    unittest.main()
