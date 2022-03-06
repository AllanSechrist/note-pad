from tkinter import Menu


class BaseMenu:
    def __init__(self, root):
        self.root = root
        self.menu_bar = Menu(root)
        self.root.config(menu=self.menu_bar)
        self.new_menu = Menu(self.menu_bar, tearoff=False)