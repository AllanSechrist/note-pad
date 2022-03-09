from tkinter import INSERT, Menu


class EditMenu():
    def __init__(self, menu_bar, text_area, root):
        self.text_area = text_area
        self.edit_menu = Menu(menu_bar, tearoff=False)
        self.edit_menu.add_command(label='Cut', command=lambda: self.cut_text(False), accelerator="Ctrl+x")
        self.edit_menu.add_command(label='Copy', command=lambda: self.copy_text(False), accelerator="Ctrl+c")
        self.edit_menu.add_command(label='Paste', command=lambda: self.paste_text(False), accelerator="Ctrl+p")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label='Undo', command=text_area.edit_undo, accelerator='Ctrl+z')
        self.edit_menu.add_command(label='Redo', command=text_area.edit_redo, accelerator='Ctrl+y')
        menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        # Edit Key Binds
        root.bind("<Control-x>", self.cut_text)
        root.bind("<Control-c>", self.copy_text)
        root.bind("<Control-y>", self.paste_text)
        self.root = root


    def cut_text(self, event):
        global selected
        if event:
            selected = self.root.clipboard_get()
        else:
            if self.text_area.selection_get():
                selected = self.text_area.selection_get()
                self.text_area.delete('sel.first', 'sel.last')
                self.root.clipboard_clear()
                self.root.clipboard_append(selected)
    

    def copy_text(self, event):
        global selected
        if event:
            selected = self.root.clipboard_get()
        if self.text_area.selection_get():
            selected = self.text_area.selection_get()
            self.root.clipboard_clear()
            self.root.clipboard_append(selected)


    def paste_text(self, event):
        global selected
        if event:
            selected = self.root.clipboard_get()
        else:
            if selected:
                position = self.text_area.index(INSERT)
                self.text_area.insert(position, selected)