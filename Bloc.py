import tkinter as tk
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser

class BlocDeNotas:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bloc de Notas")
        self.text = tk.Text(self.root, wrap="word")
        self.text.pack(expand=True, fill="both")

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Menú Archivo
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Nuevo", command=self.nuevo_archivo)
        self.file_menu.add_command(label="Abrir", command=self.abrir_archivo)
        self.file_menu.add_command(label="Guardar", command=self.guardar_archivo)
        self.file_menu.add_command(label="Eliminar", command=self.eliminar_archivo)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.root.destroy)

        # Menú Formato
        self.format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Formato", menu=self.format_menu)
        self.format_menu.add_command(label="Cambiar Fuente", command=self.cambiar_fuente)
        self.format_menu.add_command(label="Cambiar Color de Texto", command=self.cambiar_color_texto)
        self.format_menu.add_command(label="Cambiar Tamaño de Letra", command=self.cambiar_tamanio_letra)

    def nuevo_archivo(self):
        self.text.delete(1.0, tk.END)

    def abrir_archivo(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Archivos de texto", ".txt"), ("Todos los archivos", ".*")])
        if file_path:
            with open(file_path, "r") as file:
                contenido = file.read()
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, contenido)

    def guardar_archivo(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", ".txt"), ("Todos los archivos", ".*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text.get(1.0, tk.END))

    def eliminar_archivo(self):
        self.text.delete(1.0, tk.END)

    def cambiar_fuente(self):
        font_family = font.families()
        selected_font = tk.StringVar(self.root)
        selected_font.set(font_family[0])
        font_menu = tk.OptionMenu(self.root, selected_font, *font_family)
        font_menu.pack()

        def fuente():
            chosen_font = selected_font.get()
            current_font = self.text.cget("font")
            new_font = (chosen_font, current_font.split(" ")[1])
            self.text.configure(font=new_font)
            font_menu.pack_forget()

        apply_button = tk.Button(self.root, text="Aplicar", command=fuente)
        apply_button.pack()

    def cambiar_color_texto(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text.configure(fg=color)

    def cambiar_tamanio_letra(self):
        sizes = list(range(8, 81))
        selected_size = tk.StringVar(self.root)
        selected_size.set(sizes[0])
        size_menu = tk.OptionMenu(self.root, selected_size, *sizes)
        size_menu.pack()

        def tamaño():
            chosen_size = int(selected_size.get())
            current_font = self.text.cget("font")
            new_font = (current_font.split(" ")[0], chosen_size)
            self.text.configure(font=new_font)
            size_menu.pack_forget()

        apply_button = tk.Button(self.root, text="Aplicar", command=tamaño)
        apply_button.pack()

if __name__ == "__main__":
    bloc_de_notas = BlocDeNotas()
    bloc_de_notas.root.mainloop()