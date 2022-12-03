from tkinter import *
import os

root = Tk()
root.title("Python Terminal")
termf = Frame(root, width = 800, height = 400)

termf.pack(fill=BOTH, expand=YES)
wid = termf.winfo_id()
os.system('xterm -into %d -geometry 160x40 -sb -e python &' % wid)

root.mainloop()
