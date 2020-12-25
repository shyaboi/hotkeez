from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb



# Create object
root = Tk()

# Adjust size
root.geometry("1250x200")

def getValue(val):
    # w2.set(88)
    if int(val) <= 33:
        if int(val) <= 33:
            mb.showerror("Answer", "If you go lower you might not be able to see HotKeez :(")
    w2.set(val)
    roundy = int(val)/100
    print(roundy)
    root.attributes('-alpha', roundy)



leftFrame = Frame(root)
leftFrame.pack(side=LEFT)
 

label1 = Label(leftFrame, text="Left column")
label1.pack()
 
label3 = Label(leftFrame, text="Column content")
label3.pack()



w2Lable = Label(root, text='Transparentcy')
w2Lable.pack(side=TOP)
w2 = Scale(root, from_=33, to=100, length=600,tickinterval=10, orient=HORIZONTAL, command=getValue)
w2.set(88)
w2.pack()
hotkee1 = Label(root, text="HotKee 1", borderwidth=9, relief="ridge", cursor='trek', height=7, width=20)
hotkee1.pack(side=LEFT,padx=10)


hotkee2 = Label(root, text="HotKee 2", borderwidth=9, relief="ridge", cursor='trek', height=7, width=20)
hotkee2.pack(side=LEFT,padx=10)


hotkee3 = Label(root, text="HotKee 3", borderwidth=9, relief="ridge", cursor='trek', height=7, width=20)
hotkee3.pack(side=LEFT,padx=10)


hotkee4 = Label(root, text="HotKee 4", borderwidth=9, relief="ridge", cursor='trek', height=7, width=20)
hotkee4.pack(side=LEFT,padx=10)


hotkee5 = Label(root, text="HotKee 5", borderwidth=9, relief="ridge", cursor='trek', height=7, width=20)
hotkee5.pack(side=LEFT,padx=10)


hotkee6 = Label(root, text="HotKee 6", borderwidth=9, relief="ridge", cursor='trek', height=7, width=20)
hotkee6.pack(side=LEFT,padx=10)
# Execute tkinter always on top
root.call('wm', 'attributes', '.', '-topmost', '1')

root.mainloop()

