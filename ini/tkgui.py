from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("400x400")

def print_value(val):
    # w2.set(88)
    w2.set(val)
    roundy = int(val)/100
    print(roundy)
    root.attributes('-alpha', roundy)


# Create transparent window
root.attributes('-alpha',0.5)
w2 = Scale(root, from_=0, to=100, length=600,tickinterval=10, orient=HORIZONTAL, command=print_value)
w2.set(88)
w2Lable = Label(root, text='Transparentcy')
w2.pack()
w2Lable.pack()
# Execute tkinter
root.mainloop()