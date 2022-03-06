from tkinter import *
from file_menu import FileMenu

root = Tk()
root.title("Notepad")
root.geometry('800x800')

my_text = Text(root)
my_text.pack(expand=True, fill='both')

file = FileMenu(root)


if __name__=="__main__":
    root.mainloop()