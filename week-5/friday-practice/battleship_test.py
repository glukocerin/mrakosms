import unittest
import battleship

class FieldTest(unittest.TestCase):
    # def SetUp(self):
    #     self.field = [
    #                     [1,1,0,1,0,0,1,1,1,1],
    #                     [0,0,0,1,0,0,0,0,0,0],
    #                     [1,0,0,1,0,1,1,1,0,1],
    #                     [1,0,0,0,0,0,0,0,0,1],
    #                     [1,0,0,0,0,0,0,0,0,0],
    #                     [1,0,0,0,0,1,0,0,0,1],
    #                     [0,0,0,0,0,1,0,0,0,1],
    #                     [1,1,0,0,0,0,0,0,0,1],
    #                     [0,0,0,0,0,0,0,0,0,0],
    #                     [0,0,0,0,1,1,1,1,1,1]
    #                 ]

    def test_instantiate(self):
        self.assertIsInstance(battleship.Field([]), battleship.Field)


class ShipTest(unittest.TestCase):
    def test_instantiate(self):
        self.assertIsInstance(battleship.Ship('',[]), battleship.Ship)



unittest.main()
