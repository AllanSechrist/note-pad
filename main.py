from tkinter import *
from file_menu import FileMenu
from edit_menu import EditMenu
from text_window import TextArea

root = Tk()
root.title("Note")
root.geometry('800x800')

text_area = TextArea(root)
menu_bar = Menu(root)
root.config(menu=menu_bar)

file = FileMenu(root, text_area, menu_bar)
edit = EditMenu(menu_bar, text_area)


if __name__=="__main__":
    root.mainloop()