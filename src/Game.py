from tkinter import *
# from Logic import *

canvasPlayerX = 0
canvasPlayerY = 0
gridSize = 30


class StartGame(Frame):

    def __init__(self, root):
        super().__init__(root)
        self.canvas = Canvas(root, width = 800, height = 750, bg="cyan")



        self.buttonNewGame = Button(self.canvas, text = "New Game", command =  lambda: print('New Game'), bg = "blue")
        self.buttonNewGame.place(x = 100, y = 700, width = 100, height = 30)

        self.buttonQuit = Button(self.canvas, text = "Quit", command = lambda: exit(0), bg = "blue")
        self.buttonQuit.place(x = 300, y = 700, width = 100, height = 30)


        self.canvasPlayer = Canvas(self.canvas, bg = "yellow")
        self.canvasPlayer.place(x = 50, y = 50, width = 300, height = 300 )

        self.gridPlayer = [[Button(self.canvasPlayer) for i in range(0, 10)] for j in range(0, 10)]

        global canvasPlayerX
        global canvasPlayerY
        global gridSize
        xPos = canvasPlayerX
        yPos = canvasPlayerY
        for i in range(0, 10):
            for j in range(0, 10):
                self.gridPlayer[i][j].place(x = xPos, y = yPos, width = gridSize, height = gridSize)
                xPos += gridSize
            yPos += gridSize
            xPos = canvasPlayerX

        self.canvasAI = Canvas(self.canvas, bg = "green")
        self.canvasAI.place(x = 400, y = 50, width = 300, height = 300 )

        self.canvas.pack()


root = Tk()
root.title("BattleShip")
game = StartGame(root = root)
game.mainloop()
