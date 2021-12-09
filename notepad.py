# Notepad

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename

import os


def newfile():
    global file
    root.title("Untitle-Notepad")
    file = None
    TextArea.delete(1.0, END)


def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[
                           ("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[
                                 ("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None

        else:
            # save as new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file)+"-Notepad")
            print("File Saved")
    else:
        # save as new file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()


def cut():
    TextArea.event_generate(("<<Cut>>"))


def copy():
    TextArea.event_generate(("<<Copy>>"))


def peste():
    TextArea.event_generate(("<<Paste>>"))


def about():
    showinfo("Notepad", "Notepad by code with Akshay Dhongade")


root = Tk()
root.title("Notepad")
root.wm_iconbitmap("notepad2.ico")
root.geometry("500x500")

TextArea = Text(root, font="lucida 13")
file = None
TextArea.pack(fill=BOTH, expand=True)

menubar = Menu(root)

Filemenu = Menu(menubar, tearoff=0)

Filemenu.add_command(label="New", command=newfile)

Filemenu.add_command(label="Open", command=openfile)

Filemenu.add_command(label="Save", command=save)
Filemenu.add_separator()
Filemenu.add_command(label="Exit", command=quitApp)

menubar.add_cascade(label="File", menu=Filemenu)


# edit menu

Editmenu = Menu(menubar, tearoff=0)
Editmenu.add_command(label="Cut", command=cut)
Editmenu.add_command(label="Copy", command=copy)
Editmenu.add_command(label="paste", command=peste)

menubar.add_cascade(label="Edit", menu=Editmenu)


# help menu

Helpmenu = Menu(menubar, tearoff=0)
Helpmenu.add_command(label="About Notepad", command=about)

menubar.add_cascade(label="Help", menu=Helpmenu)


root.config(menu=menubar)

Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)


root.mainloop()
