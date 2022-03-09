from tkinter import filedialog, Menu
# from tkinter import *


class FileMenu():
    def __init__(self, root, text_area, menu_bar):
        self.root = root
        self.file_menu = Menu(menu_bar, tearoff=False)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Quit', command=self.close)
        menu_bar.add_cascade(label='File', menu=self.file_menu)

        self.text_area = text_area
        self.files = [("Text file", "*.txt")]


    def close(self):
        self.root.destroy()


    def open_file(self):
        file_name = filedialog.askopenfilename(initialdir='/', title="Select a file", filetypes=self.files)
        file_name = open(file_name, 'r')
        text = file_name.read()
        # Delete the text on screen
        self.text_area.delete('1.0', 'end')
        # Insert text from file_name
        self.text_area.insert('1.0', text)
        file_name.close()


    def save_as_file(self):
        text_file = filedialog.asksaveasfilename(initialdir="/", filetypes=self.files, defaultextension=self.files)

        if text_file:
            self.root.title(f'{text_file} - Note')
            text_file = open(text_file, 'w')
            text_file.write(self.text_area.get(1.0, 'end'))
            text_file.close()


    def save_file(self):
        file_name = filedialog.askopenfilename(initialdir='/', title="Select a file", filetypes=self.files)
        file_name = open(file_name, 'w')
        file_name.write(self.text_area.get(1.0, 'end'))
        file_name.close()
    