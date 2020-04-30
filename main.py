__authot__ = "Jakub Klimek"

import tkinter
from tkinter import *
from PIL import Image

root = Tk()
root.geometry("800x500")
root.title("BattleShip")

labelGamer = Label(root, text = "Player")
labelGamer.place(x = 190, y = 25)

frameGamer = Frame(root,
                   height = 300,
                   width = 300,
                   bg = "blue")
frameGamer.place(x=60, y=50)

labelComputer = Label(root, text = "Computer")
labelComputer.place(x = 560, y = 25)

frameComputer = Frame(root,
                      height = 300,
                      width = 300,
                      bg = "blue")
frameComputer.place(x=440, y=50)

pixelVirtual = PhotoImage(width = 1, height = 1)

resetButton = Button(root,
                     text = "Reset",
                     bg = "yellow",
                     image = pixelVirtual,
                     width = 240,
                     height = 50,
                     compound = "c")
resetButton.place(x = 460, y = 400)

startButton = Button(root,
                     text = "Start New Game",
                     bg = "red",
                     image = pixelVirtual,
                     width = 240,
                     height = 50,
                     compound = "c")
startButton.place( x = 75, y = 400)

root.mainloop()
