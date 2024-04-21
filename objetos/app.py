import tkinter

class App:
    
    def __init__(self, title, x, y):
        window = tkinter.Tk()
        window.title(title)
        window.minsize(width=x, height=y)
        window.mainloop()
       
Obj = App("App", 360, 640)
obj2 = App("Objeto 2", 780, 600)
App()   