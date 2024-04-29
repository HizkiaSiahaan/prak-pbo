import tkinter as tk

class SudokuCell(tk.Entry):
    def __init__(self, master, row, col, **kwargs):
        super().__init__(master, **kwargs)
        self.row = row
        self.col = col

class SudokuBoard(tk.Frame):
    def __init__(self, master, grid, **kwargs):
        super().__init__(master, **kwargs)
        self.grid = grid
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_board()

    def create_board(self):
        for i in range(9):
            for j in range(9):
                cell = SudokuCell(self, i, j, width=2, font=('Arial', 16), justify='center')
                cell.grid(row=i, column=j, ipadx=5, ipady=5)
                if self.grid[i][j] != 0:
                    cell.insert(tk.END, str(self.grid[i][j]))
                    cell.config(state=tk.DISABLED)
                self.cells[i][j] = cell

class SudokuGame(tk.Tk):
    def __init__(self, initial_grid):
        super().__init__()
        self.title("Sudoku")
        self.geometry("400x400")
        self.grid = initial_grid
        self.create_widgets()

    def create_widgets(self):
        self.board = SudokuBoard(self, self.grid)
        self.board.pack(padx=10, pady=10)

        solve_button = tk.Button(self, text="Solve", command=self.solve)
        solve_button.pack(pady=5)

    def solve(self):
        solved_grid = self.solve_sudoku(self.grid)
        if solved_grid:
            for i in range(9):
                for j in range(9):
                    self.board.cells[i][j].delete(0, tk.END)
                    self.board.cells[i][j].insert(tk.END, str(solved_grid[i][j]))
                    self.board.cells[i][j].config(state=tk.DISABLED)

    def find_empty_location(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    return row, col
        return None, None

    def is_valid_location(self, grid, row, col, num):
        for x in range(9):
            if grid[row][x] == num or grid[x][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve_sudoku(self, grid):
        row, col = self.find_empty_location(grid)
        if row is None:
            return grid
        for num in range(1, 10):
            if self.is_valid_location(grid, row, col, num):
                grid[row][col] = num
                if self.solve_sudoku(grid):
                    return grid
                grid[row][col] = 0
        return None

initial_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if __name__ == "__main__":
    game = SudokuGame(initial_grid)
    game.mainloop()