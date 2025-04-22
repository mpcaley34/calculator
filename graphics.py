from tkinter import Tk, Entry, Button


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title('Calculator')
        self.__root.geometry(f'{width}x{height}')
        self.__root.resizable(True, True)

        # Entry Widget Display
        self.__entry = Entry(self.__root, font=(
            'Arial', 24), borderwidth=2, relief='ridge', justify='right')
        self.__entry.grid(row=0, column=0, columnspan=4,
                          sticky='nsew', padx=5, pady=5)

        self.__entry.bind("<KeyPress>", self.key_input)

        # Calculator Button Layout
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        # Create buttons and place them in grid
        for row_index, row in enumerate(buttons, start=1):
            for col_index, label in enumerate(row):
                button = Button(self.__root, text=label, font=(
                    'Arial', 18), command=lambda val=label: self.on_button_click(val))
                button.grid(row=row_index, column=col_index,
                            sticky='nsew', padx=2, pady=2)

        # Make grid cells expand on Window
        for i in range(5):  # 1 for entry + 4 button rows
            self.__root.rowconfigure(i, weight=1)
        for i in range(4):  # 4 button columns
            self.__root.columnconfigure(i, weight=1)

    def on_button_click(self, val):
        if val == 'C':
            self.__entry.delete(0, 'end')
        elif val == '=':
            try:
                result = eval(self.__entry.get())
                self.__entry.delete(0, 'end')
                self.__entry.insert('end', str(result))
            except:
                self.__entry.delete(0, 'end')
                self.__entry.insert('end', 'Error')
        else:
            self.__entry.insert('end', val)

    def key_input(self, event):
        keysym = event.keysym  # This works better on macOS

        if keysym in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'plus', 'minus', 'asterisk', 'slash']:
            keymap = {
                'plus': '+',
                'minus': '-',
                'asterisk': '*',
                'slash': '/',
            }
            val = keymap.get(keysym, keysym)
            self.__entry.insert('end', val)

        elif keysym == 'Return':
            try:
                result = eval(self.__entry.get())
                self.__entry.delete(0, 'end')
                self.__entry.insert('end', str(result))
            except:
                self.__entry.delete(0, 'end')
                self.__entry.insert('end', 'Error')

        elif keysym == 'BackSpace':
            current = self.__entry.get()
            self.__entry.delete(0, 'end')
            self.__entry.insert(0, current[:-1])

        elif keysym in ['Escape', 'Delete']:
            self.__entry.delete(0, 'end')

        return "break"  # Prevents double typing

    def run(self):
        self.__root.mainloop()

    def close(self):
        self.__root.destroy()
