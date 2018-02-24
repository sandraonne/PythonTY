from tkinter import *
 
raam = Tk()
raam.title("Lipp")

tahvel = Canvas(raam, width=570, height = 350)

tahvel.create_rectangle(570, 0, 0, 150, fill="blue", outline="blue")
tahvel.create_rectangle(570, 150, 0, 200, fill="white", outline="white")
tahvel.create_rectangle(570, 200, 0, 350, fill="green", outline="green")

tahvel.pack()

raam.mainloop()