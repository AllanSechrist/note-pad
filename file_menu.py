from base_menu import BaseMenu
from tkinter import filedialog


class FileMenu(BaseMenu):
    def __init__(self, root):
        super().__init__(root)
        
        self.new_menu.add_command(label="Open", command=self.open_file)
        self.new_menu.add_command(label="Save As", command=self.save_as_file)
        self.new_menu.add_command(label="Save", command=self.save)
        self.menu_bar.add_cascade(label='File', menu=self.new_menu)

    

    def open_file(self):
        pass


    def save_as_file(self):
        pass


    def save(self):
        pass