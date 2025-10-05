import unittest

from parameterized import parameterized

from src.game_of_life import next_state, CellState
from src.game_of_life import generate_signals_for_a_cell, generate_signals_for_multiple_cells, count_signals_for_cells
from src.game_of_life import next_generation
from src.game_of_life import get_bounds


class GameOfLifeTests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    @parameterized.expand(
        [
            (CellState.DEAD, 0, CellState.DEAD),
            (CellState.DEAD, 1, CellState.DEAD),
            (CellState.DEAD, 2, CellState.DEAD),
            (CellState.DEAD, 3, CellState.ALIVE),
            (CellState.DEAD, 5, CellState.DEAD),
            (CellState.DEAD, 8, CellState.DEAD),
            (CellState.ALIVE, 1, CellState.DEAD),
            (CellState.ALIVE, 2, CellState.ALIVE),
            (CellState.ALIVE, 3, CellState.ALIVE),
            (CellState.ALIVE, 4, CellState.DEAD),
            (CellState.ALIVE, 8, CellState.DEAD),
        ]
    )
    def test_cell_behavior(self, current_state, neighbor_count, expected_output):
        self.assertEqual(next_state(current_state, neighbor_count), expected_output)

    @parameterized.expand(
        [
            ((2, 3), [(1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4)]),
            ((3, 3), [(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)]),
            ((2, 4), [(1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 3), (3, 4), (3, 5)]),
            ((0, 0), [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]),
        ]
    )
    def test_generate_signals_for_a_cell(self, cell, expected_output_signals):
        self.assertEqual(generate_signals_for_a_cell(cell), expected_output_signals)
    
    @parameterized.expand(
        [
            ([], []),
            ([(2, 3)], [(1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4),]),
            ([(2, 3), (3, 3)], [(1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4), (2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4),]),
            ([(2, 3), (3, 3), (2, 4)], [(1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4), (2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4), (1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 3), (3, 4), (3, 5),]),
        ]
    )
    def test_generate_signals_for_multiple_cells(self, cells, expected_output_signals):
        self.assertEqual(generate_signals_for_multiple_cells(cells), expected_output_signals)
    
    @parameterized.expand(
        [
            ([], {}), 
            ([(0, 0)], {(0, 0): 1}),
            ([(0, 0), (0, 1)], {(0, 0): 1, (0, 1): 1}),
            ([(0, 0), (0, 1), (0, 0)], {(0, 0): 2, (0, 1): 1}),
        ]
    )
    def test_count_signals(self, signals, expected_output_counts):
        self.assertEqual(count_signals_for_cells(signals), expected_output_counts)

    def test_next_generation_zero_cell(self):
        self.assertEqual(next_generation(set()), set())

    def test_next_generation_one_cell(self):
        self.assertEqual(next_generation({(0, 0)}), set())

    def test_next_generation_neighbor_cells(self):
        self.assertEqual(next_generation({(0, 0), (0, 1)}), set())

    def test_next_generation_triangle_cells(self):
        self.assertEqual(next_generation({(0, 0), (2, 0), (1, 1)}), {(1, 0) ,(1, 1)})
  
    def test_block_next_generation(self):
        self.assertEqual(next_generation({(0, 0), (0, 1), (1, 0), (1, 1)}), {(0, 0), (0, 1), (1, 0), (1, 1)})
    
    def test_beehive_next_generation(self):
        self.assertEqual(next_generation({(0, 1), (1, 0), (1, 2), (2, 0), (2, 2), (3, 1)}), {(0, 1), (1, 0), (1, 2), (2, 0), (2, 2), (3, 1)})
    
    def test_horizontal_blinker_next_generation(self):
        self.assertEqual(next_generation({(0, 0), (1, 0), (2, 0)}), {(1, -1), (1, 0), (1, 1)})

    def test_vertical_blinker_next_generation(self):
        self.assertEqual(next_generation({(1, -1), (1, 0), (1, 1)}), {(0, 0), (1, 0), (2, 0)})
    
    def test_glider_next_generation(self):
        self.assertEqual(next_generation({(1, 0), (2, 0), (3, 0), (3, 1), (2, 2)}), {(1, 1), (2, -1), (2, 0), (3, 0), (3, 1)})
    
    def test_get_bounds_zero_cells(self):
        self.assertEqual(get_bounds([]), ((0, 0), (10, 10)))

    def test_get_bounds_one_cell(self):
        self.assertEqual(get_bounds([(5, 5)]), ((-5, -5), (15, 15)))

    def test_get_bounds_two_cells(self):
        self.assertEqual(get_bounds([(0, 0), (20, 20)]), ((-10, -10), (30, 30)))
        
    def test_get_bounds_three_cells(self):
        self.assertEqual(get_bounds([(0, 0), (10, 10), (20, 5)]), ((-10, -10), (30, 20)))

    def test_get_bounds_four_cells(self):
        self.assertEqual(get_bounds([(10, 0), (0, 10), (5, 5), (15, 15)]), ((-10, -10), (25, 25)))

if __name__ == "__main__":
    unittest.main()

