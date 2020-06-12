from tkinter import *
from Const import *
# from Logic import *


class StartGame(Frame):
    """The class that implements the entire game object, contains all necessary methods.
        Inherits from Tk.Frame, gets 'master' as the constructor parameter."""

    def __init__(self, root):
        self.root = root
        super().__init__(self.root)
        self.canvas = Canvas(self.root, width = 850, height = 750)

        self.buttonNewGame = Button(self.canvas, text = "New Game", command =  lambda: print('New Game'), bg = "blue")
        self.buttonNewGame.place(x = 100, y = 700, width = 100, height = 30)

        self.buttonQuit = Button(self.canvas, text = "Quit", command = lambda: exit(0), bg = "blue")
        self.buttonQuit.place(x = 300, y = 700, width = 100, height = 30)

        self.canvas.pack()

        self.canvas.data = { }
        self.canvas.data["play"] = None
        self.canvas.data["stage"] = None
        self.canvas.data["axis"] = "horizontal"

        self.canvas.data["gridPlayer"] = {}
        self.canvas.data["gridAI"] = {}


        for i in range(0, 10):
            self.canvas.data["gridPlayer"][i] = {}
            for j in range(0, 10):
                self.canvas.data["gridPlayer"][i][j] = {}
                self.canvas.data["gridPlayer"][i][j]["ref"] = self.canvas.create_rectangle(GRID_SIZE + j * GRID_SIZE, GRID_SIZE + i * GRID_SIZE, GRID_SIZE * 2 + j * GRID_SIZE, GRID_SIZE * 2 + GRID_SIZE * i, fill = "red")

        for i in range(0, 10):
            self.canvas.data["gridAI"][i] = {}
            for j in range(0, 10):
                self.canvas.data["gridAI"][i][j] = {}
                self.canvas.data["gridAI"][i][j]["ref"] = self.canvas.create_rectangle(GRID_SIZE + j * GRID_SIZE + GRID_AI_TAB, GRID_SIZE + i * GRID_SIZE, GRID_SIZE * 2 + j * GRID_SIZE + GRID_AI_TAB, GRID_SIZE * 2 + GRID_SIZE * i, fill = "red")


root = Tk()
root.title("BattleShip")
game = StartGame(root = root)
game.mainloop()
