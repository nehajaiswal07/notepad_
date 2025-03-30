import os.path
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
# from tkinter.colorchooser import askcolor
import os
notepad = Tk()
notepad.title("Untitled - Notepad")
notepad.geometry("1100x650")

# notepad.configure(bg="red")

# notepad.wm_iconbitmap("icon.ico")
# -------------------------------------------
def newfile():
    global file
    notepad.title("Untitled - Notepad")
    file = None
    text.delete(1.0, END)


def openfile():
    global file
    filetype = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    file = askopenfilename(defaultextension=".txt", filetypes=filetype)
    if file == "":
        file = NONE
    else:
        notepad.title(os.path.basename(file) +  " - Notepad")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()



def save():
    global file
    filetype = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=filetype)
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()
            notepad.title(os.path.basename(file)+" - Notepad")

    else:
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()

def close():
    pass
def exit():
    notepad.destroy()

def cut():
    text.event_generate(("<<Cut>>"))

def copy():
    text.event_generate(("<<Copy>>"))


def paste():
    text.event_generate(("<<Paste>>"))
def about():
    tmsg.showinfo("Notepad", "Notepad by jais!")

# def change_back():
    # colors = askcolor(title="Change background color")
    # notepad.configure(bg=colors[1])




# ----------------------------

# file menu------------
notepad_menu = Menu(notepad)
file_m = Menu(notepad_menu, tearoff=0)
file_m.add_command(label="New", command=newfile)
file_m.add_command(label="Open", command=openfile)
file_m.add_command(label="Save", command=save)
file_m.add_command(label="Close")
file_m.add_separator()
file_m.add_command(label="Exit", command=exit)
notepad.config(menu=notepad_menu)
notepad_menu.add_cascade(label="File", menu=file_m)
# edit menu-------
edit_m = Menu(notepad_menu, tearoff=0)
edit_m.add_command(label="Cut", command=cut)
edit_m.add_command(label="Copy", command=copy)
edit_m.add_command(label="Paste", command=paste)
edit_m.add_command(label="About", command=about)

# edit_m.add_command(label="Theme", command=change_back)

notepad.config(menu = notepad_menu)
notepad_menu.add_cascade(label="Edit", menu=edit_m)
# search menu-----------

search_m = Menu(notepad_menu, tearoff=0)
search_m.add_command(label="Find")
search_m.add_command(label="Find in files")
search_m.add_command(label="Find Next")
search_m.add_command(label="Find Previous")
search_m.add_command(label="Select And Find Next")
search_m.add_command(label="Select And Find Previous")
search_m.add_command(label="Replace")
search_m.add_command(label="Go To")
search_m.add_command(label="Mark")
search_m.add_separator()
search_m.add_command(label="Style one token")
search_m.add_command(label="Jump up")
search_m.add_command(label="Jump down")
search_m.add_command(label="Bookmark")
search_m.add_command(label="Find characters in range")
notepad.config(menu=notepad_menu)
notepad_menu.add_cascade(label="Search", menu=search_m)


# view menu-----------

# view_m = Menu(notepad_menu, tearoff=0)
# view_m.add_command(label="Always on top")
# view_m.add_command(label="Toggle Full Screen Mode")
# view_m.add_command(label="Distraction Free Mode")
# view_m.add_separator()
# view_m.add_command(label="View Current File In")
# view_m.add_separator()
# view_m.add_command(label="Show Symbol")
# view_m.add_command(label="Zoom")
# view_m.add_command(label="Move/Clone Current Document")
# view_m.add_command(label="Tab")
# view_m.add_command(label="Word wrap")
# view_m.add_command(label="Hide Lines")
# view_m.add_separator()
# view_m.add_command(label="Fold All")
# view_m.add_command(label="Unfold All")
# view_m.add_separator()
# view_m.add_command(label="Summary")
# view_m.add_separator()
# view_m.add_command(label="Project Panel")
# view_m.add_command(label="Function List")
# notepad.config(menu=notepad_menu)
# notepad_menu.add_cascade(label="View", menu=view_m)



# language menu--------------------------------

language_m = Menu(notepad_menu, tearoff=0)
language_m.add_command(label="None(Normal Text)")
language_m.add_command(label="A")
language_m.add_command(label="B")
language_m.add_command(label="C")
language_m.add_command(label="D")
language_m.add_command(label="E")
language_m.add_command(label="F")
language_m.add_command(label="Gui4Cli")
language_m.add_command(label="H")
language_m.add_command(label="I")
language_m.add_command(label="J")

language_m.add_command(label="KIXtart")
language_m.add_command(label="L")
language_m.add_command(label="M")
language_m.add_command(label="N")
language_m.add_command(label="O")
language_m.add_command(label="P")
language_m.add_command(label="R")
language_m.add_command(label="S")
language_m.add_command(label="T")
language_m.add_command(label="V")
language_m.add_command(label="XML")
language_m.add_command(label="YAML")
language_m.add_separator()
language_m.add_command(label="User defined language")
language_m.add_command(label="Markdown")
notepad.config(menu=notepad_menu)
notepad_menu.add_cascade(label="Language", menu=language_m)

# settings menu---------------------------
setting_m = Menu(notepad_menu, tearoff=0)
setting_m.add_command(label="Preferences")
setting_m.add_command(label="Style Configurator")
setting_m.add_command(label="Shortcut mapper")
setting_m.add_separator()
setting_m.add_command(label="Import")
setting_m.add_separator()
setting_m.add_command(label="Edit Popup contextmenu")

notepad.config(menu=notepad_menu)
notepad_menu.add_cascade(label="Setting", menu=setting_m)

# tools menu---------------------

tool_m = Menu(notepad_menu, tearoff=0)
tool_m.add_command(label="MD5")
tool_m.add_command(label="SHA 256")
notepad.config(menu=notepad_menu)
notepad_menu.add_cascade(label="Tools", menu=tool_m)

#MACRO MENU--------------------
macro_m = Menu(notepad_menu, tearoff=0)
macro_m.add_command(label="Start Recording")
macro_m.add_command(label="Stop Recording")
macro_m.add_command(label="Playback")
macro_m.add_command(label="Save")
macro_m.add_command(label="Run Macro Multiple Times")
macro_m.add_separator()
macro_m.add_command(label="Modify")
macro_m.add_separator()
macro_m.add_command(label="Trim")
notepad.config(menu=notepad_menu)
notepad_menu.add_cascade(label="Macro", menu=macro_m)
#run menu----------------------
run_m = Menu(notepad_menu, tearoff=0)
run_m.add_command(label="Run...")
run_m.add_command(label="Get PHP Help")
run_m.add_command(label="Wikipedia search")
run_m.add_command(label="Open selected file path in new instance")
run_m.add_separator()
run_m.add_command(label="Modify shortcut/Delete")
run_m.add_separator()
notepad.config(menu=notepad_menu)
notepad_menu.add_cascade(label="Run", menu=run_m)







# ---------------scrollbar-------------------------------------------------------------

scrollbar = Scrollbar(notepad)
scrollbar.pack(side=RIGHT, fill=Y)
text = Text(notepad, yscrollcommand=scrollbar.set, font="Georgia 14 ", bg="lightgrey", width=500, height=500)
file = None
scrollbar.config(command=text.yview)
text.pack()
















notepad.mainloop()