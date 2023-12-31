import tkinter as tk
from tkinter import ttk, filedialog, Toplevel
import webbrowser
import subprocess

class Grid:
    def __init__(self, master, rows, cols):
        self.rows = rows
        self.cols = cols
        self.survivor_rules = 23
        self.birth_rules = 3
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
            file.write(str(self.survivor_rules) + '\n')
            file.write(str(self.birth_rules))



class Application:
    def __init__(self, master):
        self.master = master
        self.grid = None

        self.tab_control = ttk.Notebook(master)

        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab_help = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab3, text='Configuración del Proyecto')
        self.tab_control.add(self.tab1, text='Crear Estado Inicial')
        self.tab_control.add(self.tab2, text='Crear Esquema PDM')
        self.tab_control.add(self.tab_help, text='Ayuda')

        self.label_rows = tk.Label(self.tab1, text="Filas (N):")
        self.label_cols = tk.Label(self.tab1, text="Columnas (N):")
        self.label_survivor_rules = tk.Label(self.tab1, text="Reglas de supervivencia:")
        self.label_birth_rules = tk.Label(self.tab1, text="Reglas de nacimiento:")
        self.entry_rows = tk.Entry(self.tab1)
        self.entry_cols = tk.Entry(self.tab1)
        self.entry_survivor_rules = tk.Entry(self.tab1)
        self.entry_survivor_rules.insert(0, "23")
        self.entry_birth_rules = tk.Entry(self.tab1)
        self.entry_birth_rules.insert(0, "3")
        self.button_create = tk.Button(self.tab1, text='Crear cuadrícula', command=self.create_grid)
        self.button_export = tk.Button(self.tab1, text='Exportar estado ', command=self.export_grid)
        
        self.label_rows_2 = tk.Label(self.tab2, text="Filas (N):")
        self.label_cols_2 = tk.Label(self.tab2, text="Columnas (N):")
        self.label_status = tk.Label(self.tab2, text="")  
        self.pdm_rows = tk.Entry(self.tab2)
        self.pdm_cols = tk.Entry(self.tab2)
        self.button_generate_pdm = tk.Button(self.tab2, text='Generar PDM', command=lambda: self.generate_pdm(int(self.pdm_rows.get()), int(self.pdm_cols.get())))

        self.label_rows.grid(row=0, column=0, padx=5, pady=5)
        self.label_cols.grid(row=0, column=1, padx=5, pady=5)
        self.entry_rows.grid(row=1, column=0, padx=5, pady=5)
        self.entry_cols.grid(row=1, column=1, padx=5, pady=5)
        self.label_survivor_rules.grid(row=3, column=0, padx=5, pady=5)
        self.label_birth_rules.grid(row=3, column=1, padx=5, pady=5)
        self.entry_survivor_rules.grid(row=4, column=0, padx=5, pady=5)
        self.entry_birth_rules.grid(row=4, column=1, padx=5, pady=5)
        self.button_create.grid(row=1, column=2, padx=5, pady=5)
        self.button_export.grid(row=1, column=3, padx=5, pady=5)
        
        self.label_rows_2.grid(row=0, column=0, padx=5, pady=5)
        self.label_cols_2.grid(row=0, column=1, padx=5, pady=5)
        self.pdm_rows.grid(row=1, column=0, padx=5, pady=5)
        self.pdm_cols.grid(row=1, column=1, padx=5, pady=5)
        self.button_generate_pdm.grid(row=1, column=2, padx=5, pady=5)
        self.label_status.grid(row=1, column=3, padx=5, pady=5)  


        self.button_set_powerdevs = tk.Button(self.tab3, text='Setear PowerDEVS', command=self.set_powerdevs)
        self.button_reset_original = tk.Button(self.tab3, text='Restablecer a versión Original', command=self.reset_original)

        self.button_set_powerdevs.pack()
        self.button_reset_original.pack()

        self.tab_control.bind("<<NotebookTabChanged>>", self.tab_changed)

        self.tab_control.pack(expand=1, fill='both')

    def create_grid(self):
        rows = int(self.entry_rows.get())
        cols = int(self.entry_cols.get())
        if self.grid is not None:
            self.grid.frame.destroy()
        self.grid = Grid(self.tab1, rows, cols)

    def export_grid(self):
        if self.grid is not None:
            self.grid.survivor_rules = int(self.entry_survivor_rules.get())
            self.grid.birth_rules = int(self.entry_birth_rules.get())
            self.grid.export()

    def generate_pdm(self, N, M):
        from gen_template import generate_pdm
        output_file = "../examples/gol/generated_{0}x{1}.pdm".format(N, M)
        generate_pdm(N, M, output_file)    
        self.label_status.config(text="Listo!", fg="green")

    # Functions for the buttons in tab 3
    def set_powerdevs(self):
        print("Setting PowerDEVS...")
        subprocess.run(["bash", "./build.sh"])

    def reset_original(self):
        print("Resetting to original version...")
        subprocess.run(["bash", "./restore.sh"])

    # Function for the Help button
    def open_help_window(self):
        help_window = Toplevel(self.master)
        help_window.title('Ayuda')

        guide_button = tk.Button(help_window, text='Guía de uso', command=self.open_help)
        about_button = tk.Button(help_window, text='Acerca de', command=self.open_about)

        guide_button.pack()
        about_button.pack()

    def open_help(self):
        print("Opening help...")
        

    def open_about(self):
        print("Opening about...")

    def tab_changed(self, event):
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")

        if tab_text == "Ayuda":
            self.open_help_window()

root = tk.Tk()
root.title("PowerDEVS - Settings Game of Life (GoL)") 
app = Application(root)
root.mainloop()

