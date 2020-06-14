from tkinter import *
from tkinter import messagebox
from Const import *
# from Logic import *


class StartGame(object):

    def printAttentionMessage(self):
        # print("Method which print information about the wrong placing of the ship!")
        messagebox.showwarninig("Warning", "Ustaw statek zgodnie z zasadami!!!")

    def aiClick(self):
        # print("Ai put ship!")
        pass

    def playerClick(self):
        # print("Player put ship!")
        pass

    def quitGame(self):
        # print("Function which quit from game!")
        self.root.destroy()
        exit(0)

    def newGame(self):
        # print("Function which start New Game!")
        pass

    def resetGame(self):
        # print("Function which reset game!")
        pass

    def rotateShip(self):
        # print("Function to change direction vertical/horizontal.")
        pass

    def checkDistance(self):
        # print("Function which check distance to ships!")
        pass

    def playerSpaceAroundShip(self):
        # print("Function which ensure free space around the ship!")
        pass

    def aiSpaceAroundShip(self):
        # print("Function which ensure free space around the ship!")
        pass

    def playerShotShip(self):
        # print("Function that supports the user's shot!")
        pass

    def aiShotShip(self):
        # print("Function that supports the ai shot!")
        pass

    def getWinner(self):
        # print("Function that checks the win condition!")
        pass

    def __init__(self, root):
        self.root = root

        self.buttonNewGame = Button(self.root, text = "New Game", height = 2, width = 10, bg = "lightsteelblue", command = self.newGame)
        self.buttonQuit = Button(self.root, text = "Quit", height = 2, width = 10, bg = "lightsteelblue", command = self.quitGame)
        self.buttonReset = Button(self.root, text = "Reset", height = 2, width = 10, bg = 'lightsteelblue', command = self.resetGame)
        self.buttonRotate = Button(self.root, text = "Rotate", height = 2, width = 10, bg = 'lightsteelblue', command = self.rotateShip)

        self.gridPlayer = [[0 for i in range(10)] for j in range(10)]
        self.gridAi = [[0 for i in range(10)] for j in range(10)]

        for i in range(10):
            for j in range(10):
                self.gridPlayer[i][j] = Button(self.root, height = 2, width = 3, bg = 'silver', command = lambda i=i, j=j: self.playerClick(i, j))
                self.gridPlayer[i][j].grid(row = i+3, column = j + 1)

        self.textPlayerMap = Label(self.root, height = 3, width = 63, text = "Player Map")
        self.textPlayerMap.grid(row = 1, column = 1, columnspan = 10)

        self.textAIMap = Label(self.root, height = 3, width = 62, text = 'AI Map')
        self.textAIMap.grid(row = 1, column = 13, columnspan = 10)

        for i in range(10):
            for j in range(10):
                self.gridAi[i][j] = Button(self.root, height = 2, width = 3, bg = 'grey', command = lambda i=i, j=j: self.aiClick(i, j))
                self.gridAi[i][j].grid(row = i+3, column = j + 13)

        self.root.grid_columnconfigure(11, minsize = 22)
        self.buttonNewGame.grid(row=3, column=25, columnspan = 2)
        self.buttonReset.grid(row=5, column=25, columnspan = 2)
        self.buttonRotate.grid(row=7, column=25, columnspan = 2)
        self.buttonQuit.grid(row=9, column=25, columnspan = 2)


# Program Start :)
root = Tk()
root.title("BattleShip")
game = StartGame(root = root)
root.mainloop()
