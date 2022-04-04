
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfile, asksaveasfilename
from turtle import right
from tkinter.messagebox import showinfo
import os

def newfile():
    global file
    root.title("Untitled-Notepad")
    file=None
    TextArea.delete(1.0, END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",
    filetypes=[("All Files","*.*"),
    ("Text Documents","*.txt")])

    if file == "":
        file = None 
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0,END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def savefile():
    global file 
    if file == None:
        file = asksaveasfilename(initialfile= 'Untitled.txt',defaultextension=".txt",
    filetypes=[("All Files","*.*"),
    ("Text Documents","*.txt")])

        if file == "":
           file = None

        else:
        #SAVE AS NEW FILE 
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file) + " -Notepad")
            print("File Saved")

    else:
        #SAVE THE FILE
        f = open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
        


def quitapp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("NotePad", "Created by Pallavi")

if __name__ == '__main__':
    #BASIC TKINTER SETUP
    root = Tk()
    root.title("Untitled-Notepad")
    root.geometry("644x788")

    #ADD TEXTAREA
    TextArea = Text(root,font="lucida 13")
    file = None
    TextArea.pack(fill=BOTH, expand=True)

    #LETS CREATE A MENUBAR 
    MenuBar = Menu(root)

    #FILE MENU STARTS
    FileMenu = Menu(MenuBar,tearoff=0)

    #TO OPEN NEW FILE
    FileMenu.add_command(label="New", command=newfile)

    #TO OPEN EXISTING FILE
    FileMenu.add_command(label="Open", command=openfile)

    #TO SAVE CURRENT FILE
    FileMenu.add_command(label="Save", command=savefile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitapp)
    MenuBar.add_cascade(label="File",menu=FileMenu)
    #FILE MENU END

    #EDIT MENU STARTS
    EditMenu = Menu(MenuBar,tearoff=0)

    #TO GIVE FEATURE OF CUT,COPY AND PASTE 
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)

    MenuBar.add_cascade(label="Edit",menu=EditMenu)
    #EDIT MENU END

    #HELP MENU STARTS
    HelpMenu = Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about) 

    MenuBar.add_cascade(label="Help",menu=HelpMenu)
    #HELP MENU END
    root.config(menu=MenuBar)

    #ADDING SCROLLBAR
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)


    root.mainloop()
