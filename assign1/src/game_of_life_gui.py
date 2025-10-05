import tkinter as tk
import ast
import sys
import os

from src.game_of_life import next_generation, get_bounds

def read_initial_cells(file_path):
    file_path = os.path.join(os.path.dirname(__file__), file_path)
    
    with open(file_path, 'r') as file:
        return set(ast.literal_eval(f"({file.read().strip()})"))

def draw_cells(cells, canvas):
    if not cells:
        return

    (min_x, min_y), (max_x, max_y) = get_bounds(cells)
    canvas.config(width=(max_x - min_x + 1) * 10, height=(max_y - min_y + 1) * 10)
    
    canvas.delete("all")
    for x, y in cells:
        canvas.create_rectangle((x - min_x) * 10, (y - min_y) * 10,
                                (x - min_x + 1) * 10, (y - min_y + 1) * 10, fill="black")

def update_generation(live_cells, canvas, root):
    next_gen = next_generation(live_cells)
    draw_cells(next_gen, canvas)
    root.after(1000, lambda: update_generation(next_gen, canvas, root))
        
def create_game_of_life_gui():
    root = tk.Tk()
    root.title("Game of Life")

    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    live_cells = read_initial_cells('initial_cells.txt')

    update_generation(live_cells, canvas, root)

    root.mainloop()

if __name__ == "__main__":
    create_game_of_life_gui()

