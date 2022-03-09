from file_menu import FileMenu
from edit_menu import EditMenu
from tkinter import *


class NotePad(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Note")
        self.geometry('800x800')
        menu_bar = Menu(self)
        self.config(menu=menu_bar)
        text_area = Text(self, undo=True)
        text_area.pack(expand=True, fill='both')
        self.file_menu = FileMenu(self, text_area, menu_bar)
        self.edit_menu = EditMenu(menu_bar, text_area, self)


if __name__=="__main__":
    app = NotePad()
    app.mainloop()