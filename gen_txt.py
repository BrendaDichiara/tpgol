import tkinter as tk
from tkinter import ttk, filedialog

class Grid:
    def __init__(self, master, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = [[0 for _ in range(cols)] for _ in range(rows)]
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.frame = tk.Frame(master)

        for i in range(rows):
            for j in range(cols):
                self.buttons[i][j] = tk.Button(self.frame, width=2, height=1, bg='white', bd=1, relief="solid", command=lambda i=i, j=j: self.click(i, j))
                self.buttons[i][j].grid(row=i, column=j, padx=0, pady=0)

        self.frame.grid(row=2, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

    def click(self, i, j):
        self.cells[i][j] = 1 - self.cells[i][j]
        self.buttons[i][j].config(bg='black' if self.cells[i][j] else 'white')

    def export(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text file", "*.txt"),("All Files", "*.*")))
        with open(filename, 'w') as file:
            file.write(str(self.rows) + '\n')
            file.write(str(self.cols) + '\n')
            for i in range(self.rows):
                for j in range(self.cols):
                    file.write(str(self.cells[i][j]))
                file.write('\n')

class Application:
    def __init__(self, master):
        self.master = master
        self.grid = None

        self.tab_control = ttk.Notebook(master)

        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab4 = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab1, text='Crear Estado Inicial')
        self.tab_control.add(self.tab2, text='Crear Esquema PDM')
        self.tab_control.add(self.tab3, text='Configuración del Proyecto')
        self.tab_control.add(self.tab4, text='Help')

        self.entry_rows = tk.Entry(self.tab1)
        self.entry_cols = tk.Entry(self.tab1)
        self.button_create = tk.Button(self.tab1, text='Crear cuadrícula', command=self.create_grid)
        self.button_export = tk.Button(self.tab1, text='Exportar txt', command=self.export_grid)

        self.entry_rows.grid(row=0, column=0, padx=5, pady=5)
        self.entry_cols.grid(row=0, column=1, padx=5, pady=5)
        self.button_create.grid(row=0, column=2, padx=5, pady=5)
        self.button_export.grid(row=0, column=3, padx=5, pady=5)

        self.tab_control.pack(expand=1, fill='both')

    def create_grid(self):
        rows = int(self.entry_rows.get())
        cols = int(self.entry_cols.get())
        if self.grid is not None:
            self.grid.frame.destroy()
        self.grid = Grid(self.tab1, rows, cols)

    def export_grid(self):
        if self.grid is not None:
            self.grid.export()

root = tk.Tk()
app = Application(root)
root.mainloop()
