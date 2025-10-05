from enum import Enum

class CellState(Enum):
    ALIVE = 1
    DEAD = 2

def next_state(current_state, number_of_live_neighbors):
    return CellState.ALIVE if number_of_live_neighbors == 3 or (current_state == CellState.ALIVE and number_of_live_neighbors == 2) else CellState.DEAD

def generate_signals_for_a_cell(cell):
    x, y = cell
    return [
        (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
        (x, y - 1),                 (x, y + 1),
        (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)
    ]

def generate_signals_for_multiple_cells(cells):
    return sum((generate_signals_for_a_cell(cell) for cell in cells), [])

def count_signals_for_cells(signals):
    return {cell: signals.count(cell) for cell in signals}

def next_generation(cells):
    cells_and_signals_count = count_signals_for_cells(generate_signals_for_multiple_cells(cells))
    
    def becomes_alive(cell, number_of_live_neighbors):
        return next_state(CellState.ALIVE if cell in cells else CellState.DEAD, number_of_live_neighbors) == CellState.ALIVE
    
    return set([cell for cell, number_of_live_neighbors in cells_and_signals_count.items() if becomes_alive(cell, number_of_live_neighbors)])

def get_bounds(points):
    OFFSET = 10

    if not points:
        return ((0, 0), (OFFSET, OFFSET))

    x_points, y_points = [x for x, _ in points], [y for _, y in points]

    return ((min(x_points) - OFFSET, min(y_points) - OFFSET), (max(x_points) + OFFSET, max(y_points) + OFFSET))

