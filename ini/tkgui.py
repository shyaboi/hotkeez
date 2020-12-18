from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("400x400")

def setVal():
    print(w2.get())
# Create transparent window
root.attributes('-alpha',0.5)
w2 = Scale(root, from_=0, to=200, length=600,tickinterval=10, orient=HORIZONTAL)
w2.set(23)
w2.pack()
# Execute tkinter
root.mainloop()