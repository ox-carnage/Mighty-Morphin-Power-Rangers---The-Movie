import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto")

        # Criação das janelas de texto
        self.text_area1 = tk.Text(self.root)
        self.text_area1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.text_area2 = tk.Text(self.root)
        self.text_area2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Criação da janela de visualização
        self.preview_area = tk.Text(self.root, bg='light grey')
        self.preview_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Criação do menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Arquivo", menu=self.file_menu)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Salvar", command=self.save_file)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        file = open(file_path, 'r')
        content = file.read()
        self.text_area1.delete('1.0', tk.END)
        self.text_area1.insert('1.0', content)
        self.update_preview()

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        content = self.text_area2.get('1.0', 'end')
        file = open(file_path, 'w')
        file.write(content)
        file.close()

    def update_preview(self):
        # Atualiza a janela de visualização com o conteúdo da segunda janela de texto
        self.preview_area.delete('1.0', tk.END)
        self.preview_area.insert('1.0', self.text_area2.get('1.0', tk.END))

root = tk.Tk()
te = TextEditor(root)
root.mainloop()
