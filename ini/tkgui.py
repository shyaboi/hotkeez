from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
# Create object
root = Tk()

# Adjust size
root.geometry("800x200")

def getValue(val):
    # w2.set(88)
    if int(val) <= 33:
        if int(val) <= 33:
            mb.showerror("Answer", "If you go lower you might not be able to see HotKeez :(")
    w2.set(val)
    roundy = int(val)/100
    print(roundy)
    root.attributes('-alpha', roundy)




# tk.Button(text='Answer', command=answer).pack(fill=tk.X)
leftFrame = Frame(root)
leftFrame.pack(side=LEFT)
 
rightFrame = Frame(root)
rightFrame.pack(side=RIGHT)
 
label1 = Label(leftFrame, text="Left column")
label1.pack()
 
label3 = Label(leftFrame, text="Column content")
label3.pack()
 
label2 = Label(rightFrame, text="Right column")
label2.pack()


w2Lable = Label(root, text='Transparentcy')
w2Lable.pack(side=TOP)
w2 = Scale(root, from_=33, to=100, length=600,tickinterval=10, orient=HORIZONTAL, command=getValue)
w2.set(88)
w2.pack()
label2 = Label(root, text="HotKeez 1", borderwidth=9, relief="ridge", cursor='trek', height=7, width=20)
label2.pack(side=LEFT,padx=10)
label2 = Label(root, text="HotKeez 2", borderwidth=9, relief="ridge", cursor='trek', height=7, width=20)
label2.pack(side=LEFT,padx=10)
label2 = Label(root, text="HotKeez 3", borderwidth=9, relief="ridge", cursor='trek', height=7, width=20)
label2.pack(side=LEFT,padx=10)
label2 = Label(root, text="HotKeez 4", borderwidth=9, relief="ridge", cursor='trek', height=7, width=20)
label2.pack(side=LEFT,padx=10)
label2 = Label(root, text="HotKeez 5", borderwidth=9, relief="ridge", cursor='trek', height=7, width=20)
label2.pack(side=LEFT,padx=10)
label2 = Label(root, text="HotKeez 6", borderwidth=9, relief="ridge", cursor='trek', height=7, width=20)
label2.pack(side=LEFT,padx=10)
# Execute tkinter always on top
root.call('wm', 'attributes', '.', '-topmost', '1')
root.mainloop()