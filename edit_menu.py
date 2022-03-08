from tkinter import INSERT, Menu


class EditMenu():
    def __init__(self, menu_bar, text_area):
        self.text_area = text_area
        self.edit_menu = Menu(menu_bar, tearoff=False)
        self.edit_menu.add_command(label='Cut', command=lambda: self.cut_text(False))
        self.edit_menu.add_command(label='Copy', command=lambda: self.copy_text(False))
        self.edit_menu.add_command(label='Paste', command=lambda: self.paste_text(False))
        self.edit_menu.add_command(label='Undo', command=lambda: self.undo_text(False))
        self.edit_menu.add_command(label='Redo', command=lambda: self.redo_text(False))
        menu_bar.add_cascade(label="Edit", menu=self.edit_menu)


    def cut_text(self, e):
        global selected
        if self.text_area.selection_get():
            selected = self.text_area.selection_get()
            self.text_area.delete('sel.first', 'sel.last')

    
    def copy_text(self, e):
        pass


    def paste_text(self, e):
        if selected:
            position = self.text_area.index(INSERT)
            self.text_area.insert(position, selected)

    
    def undo_text(self, e):
        pass

    
    def redo_text(self, e):
        pass