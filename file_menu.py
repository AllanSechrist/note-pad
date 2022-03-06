from base_menu import BaseMenu
from tkinter import filedialog


class FileMenu(BaseMenu):
    def __init__(self, root, text_area):
        super().__init__(root)
        
        self.new_menu.add_command(label="Open", command=self.open_file)
        self.new_menu.add_command(label="Save As", command=self.save_as_file)
        self.new_menu.add_command(label="Save", command=self.save_file)
        self.menu_bar.add_cascade(label='File', menu=self.new_menu)

        self.text_area = text_area
        self.files = [("Text file", "*.txt")]


    def open_file(self):
        file_name = filedialog.askopenfilename(initialdir='/', title="Select a file", filetypes=self.files)
        file_name = open(file_name, 'r')
        text = file_name.read()

        self.text_area.insert('end', text)
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
    