import unittest
from app import gol

class TestUniverse(unittest.TestCase):
    def setUp(self):
        self.three_by_three = "000000000"
        self.three_by_three_short = "00000000"
    
    def test_empty_string(self):
        """ Testing empty string """
        self.assertEqual(gol.string_to_universe('', 3), [])

    def test_zero_width(self):
        """ Testing zero width """
        self.assertEqual(gol.string_to_universe(self.three_by_three, 0), [])

    def test_string_not_divisible_by_width(self):
        """ Testing extra characters are dropped """
        self.assertEqual(gol.string_to_universe(self.three_by_three_short, 3), \
                [[0, 0, 0], [0, 0, 0]])

    def test_string_to_universe(self):
        """ Testing happy path scenario """
        self.assertEqual(gol.string_to_universe(self.three_by_three, 3), \
                [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

class TestNeighbors(unittest.TestCase):
    def setUp(self):
        self.single_cell = [[0]]
        self.three_by_three_singleton = gol.string_to_universe("000010000", 3)
        self.three_by_three_multiple = gol.string_to_universe("000011011", 3)

    def test_neighbor_addresses(self):
        self.assertEqual(gol.neighbor_addy(1, 1), [\
        [0,0],[0,1],[0,2], \
        [1,0],[1,2], \
        [2,0],[2,1],[2,2]])

    def test_neighbor_addresses_corner(self):
        self.assertEqual(gol.neighbor_addy(0, 0), [\
        [-1,-1],[-1,0],[-1,1], \
        [0,-1],[0,1], \
        [1,-1],[1,0],[1,1]])

    def test_valid_address(self):
        self.assertEqual(gol.address_valid(1, 1, 3, 3), True)

    def test_valid_address_off_left(self):
        self.assertEqual(gol.address_valid(1, -1, 3, 3), False)

    def test_valid_address_off_right(self):
        self.assertEqual(gol.address_valid(1, 3, 3, 3), False)

    def test_valid_address_off_top(self):
        self.assertEqual(gol.address_valid(-1, 1, 3, 3), False)

    def test_valid_address_off_bottom(self):
        self.assertEqual(gol.address_valid(3, 1, 3, 3), False)

    def test_list_of_neighbors(self):
        self.assertEqual(gol.neighbor_population(self.single_cell, 1, 0, 0), 0)

    def test_zero_neighbors_center(self):
        """ Single cell no neighbors """
        self.assertEqual(gol.neighbor_population(self.three_by_three_singleton, 3, 1, 1), 0)

    def test_one_neighbor_top_corner(self):
        """ Multiple cell top left corner """
        self.assertEqual(gol.neighbor_population(self.three_by_three_multiple, 3, 0, 0), 1)

    def test_zero_neighbors_lower_corner(self):
        """ Single cell no neighbors """
        self.assertEqual(gol.neighbor_population(self.three_by_three_multiple, 3, 2, 2), 3)

class TestGeneration(unittest.TestCase):
    def setUp(self):
        self.cell_active_zero_neighbors = gol.string_to_universe("000010000", 3)
        self.cell_active_one_neighbor = gol.string_to_universe("000011000", 3)
        self.cell_active_two_neighbors = gol.string_to_universe("001011000", 3)
        self.cell_active_three_neighbors = gol.string_to_universe("001011010", 3)
        self.cell_active_four_neighbors = gol.string_to_universe("101011010", 3)
        self.cell_active_five_neighbors = gol.string_to_universe("101011110", 3)
        self.cell_active_full = gol.string_to_universe("111111111", 3)
        self.cell_inactive_two_neighbors = gol.string_to_universe("010001000", 3)
        self.cell_inactive_three_neighbors = gol.string_to_universe("100100001", 3)
        self.cell_inactive_one_neighbor = gol.string_to_universe("000100000", 3)
        self.cell_inactive_four_neighbors = gol.string_to_universe("010101010", 3)


    def test_generation_cell_active_zero_neighbors(self):
        """ Testing zero neighbors, cell should die or stay dead """
        self.assertEqual(gol.generation(self.cell_active_zero_neighbors, 3, 1, 1), 0)

    def test_generation_cell_active_one_neighbor(self):
        """ Testing one neighbor, cell should die as if by solitude """
        self.assertEqual(gol.generation(self.cell_active_one_neighbor, 3, 1, 1), 0)

    def test_generation_cell_active_two_neighbor(self):
        """ Testing two neighbors, cell should live """
        self.assertEqual(gol.generation(self.cell_active_two_neighbors, 3, 1, 1), 1)

    def test_generation_cell_active_three_neighbor(self):
        """ Testing three neighbors, cell should live """
        self.assertEqual(gol.generation(self.cell_active_three_neighbors, 3, 1, 1), 1)

    def test_generation_cell_active_four_neighbor(self):
        """ Testing four neighbors, cell should die as if by overpopulation """
        self.assertEqual(gol.generation(self.cell_active_four_neighbors, 3, 1, 1), 0)

    def test_generation_cell_active_five_neighbor(self):
        """ Testing four neighbors, cell should die as if by overpopulation """
        self.assertEqual(gol.generation(self.cell_active_five_neighbors, 3, 1, 1), 0)

    def test_generation_cell_active_full(self):
        """ Testing four neighbors, cell should die as if by overpopulation """
        self.assertEqual(gol.generation(self.cell_active_full, 3, 1, 1), 0)

    def test_generation_cell_inactive_one_neighbors(self):
        """ Testing inactive cell with one neighbor, cell should stay dead """
        self.assertEqual(gol.generation(self.cell_inactive_one_neighbor, 3, 1, 1), 0)

    def test_generation_cell_inactive_two_neighbors(self):
        """ Testing inactive cell with two neighbors, cell should stay dead """
        self.assertEqual(gol.generation(self.cell_inactive_two_neighbors, 3, 1, 1), 0)

    def test_generation_cell_inactive_three_neighbors(self):
        """ Testing inactive cell with three neighbors, cell should come alive"""
        self.assertEqual(gol.generation(self.cell_inactive_three_neighbors, 3, 1, 1), 1)

    def test_generation_cell_inactive_four_neighbors(self):
        """ Testing inactive cell with four neighbors, cell should stay dead """
        self.assertEqual(gol.generation(self.cell_inactive_four_neighbors, 3, 1, 1), 0)