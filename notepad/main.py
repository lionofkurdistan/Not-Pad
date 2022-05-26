from cgitb import text
import contextlib
from fileinput import close
from importlib.resources import contents
from tkinter import *
from tkinter import filedialog
from click import open_file

from imageio import save
from pkg_resources import ContextualVersionConflict

root = Tk()
root.title("Not Pad By Lion Of Kurdistan")
root.geometry("600x600")
root.config(bg='lightblue')
root.resizable(False,False)

def save_file():
    open_file = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if open_file is None :
        return
    text = str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()
    
    
def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('text files','*.txt')])
    if file is not None:
        content = file.read()
    entry.insert(INSERT,content )

b1 = Button(root,width='20',height='2',bg='#fff',text='save file',command=save_file).place(x=100,y=5)
b2 = Button(root,width='20',height='2',bg='#fff',text='open file',command=open_file).place(x=300,y=5)

entry = Text(root,height='33', width='72', wrap=WORD)
entry.place(x=10,y=60)


root.mainloop()