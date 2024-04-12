import tkinter

window = tkinter.Tk()
window.title("Notepad Marcos")
window.geometry("1280x720")
# window.minsize(width=720, height=720)

text_area = tkinter.Text(window, font="Arial 20 bold")
text_area.pack()

window.mainloop()
