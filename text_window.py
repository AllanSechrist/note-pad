from tkinter import Text

# user_text = Text(root)
# user_text.pack(expand=True, fill='both')

class TextArea(Text):
    def __init__(self, root):
        super().__init__(root, undo=True)
        self.pack(expand=True, fill='both')


    