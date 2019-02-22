import tkinter as tk


class Yzmgui(tk.Frame):
    """docstring for yzmgui"""

    def __init__(self, root, image, name):
        super().__init__(root)
        root.title(name)
        root['bg'] = 'DarkGray'
        self.yzm = None
        self.pack()
        img = tk.PhotoImage(file=image)
        self.image_name = img.zoom(2, 2)
        self.contents = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.Imagelable = tk.Label()
        self.Imagelable['image'] = self.image_name
        self.Imagelable.pack(side='top')
        self.entry = tk.Entry()
        self.entry.pack()
        # self.contents.set("this is a variable")
        self.entry["textvariable"] = self.contents
        self.entry.bind('<Key-Return>', self.bindevent)
        self.button = tk.Button()
        self.button['text'] = 'submit'
        self.button['fg'] = 'red'
        self.button['bg'] = 'black'
        self.button['command'] = self.submit
        self.button.pack(side='bottom')

    def bindevent(self, event):
        result = self.contents.get()
        self.yzm = result
        self.quit()

    def submit(self):
        result = self.contents.get()
        self.yzm = result
        self.quit()


def yzm(name, img):
    root = tk.Tk()
    root.geometry("300x140+500+400")
    yzmgui = Yzmgui(root, img, name)
    yzmgui.mainloop()
    root.destroy()
    return yzmgui.yzm


if __name__ == '__main__':
    filename = 'yzm.png'
    result = yzm(filename)
    print(result)
