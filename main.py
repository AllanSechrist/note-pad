from tkinter import *
from file_menu import FileMenu
from text_window import TextArea

root = Tk()
root.title("Note")
root.geometry('800x800')

text_area = TextArea(root)

file = FileMenu(root, text_area)


if __name__=="__main__":
    root.mainloop()