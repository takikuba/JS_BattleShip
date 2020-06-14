from tkinter import *
from tkinter import messagebox
from Const import *
from random import *


def getWinner():
    """Metchod which checks the winning condition."""
    # print("Function that checks the win condition!")
    global aiShipPos
    global playerShipPos

    if (len(aiShipPos) == 0) and (countShip >= 10):
        messagebox.showinfo("", "Wygrana!")
    elif (len(playerShipPos) == 0) and (countShip >= 10):
        messagebox.showinfo("", "Przegrana!")


def printAttentionMessage():
    """Method which print information about the wrong placing of the ship."""
    messagebox.showwarning("Warning", "Ustaw statek zgodnie z zasadami!!!")


def newGame():
    """Method which allow to start the game."""
    # print("Function which start New Game!")
    global startGame
    startGame = True


def placeShip1(x, row, col, times, i):
    """Method which update ship co-ordinates.
        :param x: the name of variable to change,
        :param row: row number of ship
        :param col: column number of ship
        :param times: size of ship
        :param i: size of ship on other axis

        :return: update list"""
    # print("Function get space, and returned modify.")

    x.append((row - 1, col))
    x.append((row - 1, col + 1))
    x.append((row - 1, col - 1))
    x.append((row + times, col))
    x.append((row + times, col + 1))
    x.append((row + times, col - 1))
    x.append((row + i, col + 1))
    x.append((row + i, col - 1))

    return x


def placeShip3(x, row, col, times, i):
    """Method which update ship co-ordinates.
        :param x: the name of variable to change,
        :param row: row number of ship
        :param col: column number of ship
        :param times: size of ship
        :param i: size of ship on other axis

        :return: update list"""
    # print("Function get space, and returned modify.")

    x.append((row, col - 1))
    x.append((row + 1, col - 1))
    x.append((row - 1, col - 1))
    x.append((row, col + times))
    x.append((row + 1, col + times))
    x.append((row - 1, col + times))
    x.append((row + 1, col + i))
    x.append((row - 1, col + i))

    return x


class StartGame(object):
    """A class to represented game object."""

    def aiShip(self, times, exception):
        """Method which placing AI ships on the map, and add position to array.
            :param times: number of iterations
            :param exception: number to subtraction of the rows/columns number"""

        global aiShipPos
        global aiSpace

        tmp = []
        position = randrange(2)

        if position == 1:
            row = randrange(10 - exception)
            col = randrange(10)
            for i in range(times):
                tmp.append((row + i, col))

            if (not [el for el in aiShipPos if el in tmp]) and (not [el for el in aiSpace if el in tmp]):
                for i in range(times):
                    aiShipPos.append((row + i, col))
                    self.aiSpaceAroundShip(position, row, col, times, i)
            else:
                self.aiShip(times, exception)
        else:
            row = randrange(10)
            col = randrange(10 - exception)
            for i in range(times):
                tmp.append((row, col + i))
            if (not [el for el in aiShipPos if el in tmp]) and (not [el for el in aiSpace if el in tmp]):
                for i in range(times):
                    aiShipPos.append((row, col + i))

                    self.aiSpaceAroundShip(position, row, col, times, i)
            else:
                pass

    def aiClick(self, row, col):
        """Method which protects the mechanism of shooting to AI ship.
            :param row: the row number where shot
            :param col: the col number where shot"""
        # print("Click on ai map!")
        global startGame
        global countShip
        global planeNumber
        global aiShipPos

        if startGame:
            if (len(aiShipPos) > 0) and (countShip >= 10):
                self.__gridAi[row][col].configure(bg="black", relief=SUNKEN)
                self.aiShotShip(row, col)
                planeNumber += 1
                self.playerShotShip()
            else:
                messagebox.showinfo("", "Rozmiesc wszystkie statki!")

            getWinner()
        else:
            messagebox.showinfo("", "Gra nie rozpoczeta!")

    def playerClick(self, row, col):
        """Methods which supports the player placement of ships.
            :param row: the row number where ship place
            :param col: the column number where ship place."""
        # print("Player put ship!")
        global countShip
        global rotateShip
        global countDown
        global playerSpace

        position = rotateShip % 2
        if position == 1:
            pass
        else:
            if countShip < 4:
                if self.checkDistance(position, row, col, 1) == False:
                    printAttentionMessage()
                    countShip -= 1
            elif countShip < 7:
                if (col + 1) >= 10:
                    printAttentionMessage()
                    countShip -= 1
                elif (col + 1) < 10:
                    if self.checkDistance(position, row, col, 2) == False:
                        printAttentionMessage()
                        countShip -= 1
                if countShip < 4:
                    if self.checkDistance(position, row, col, 1) == False:
                        printAttentionMessage()
                        countShip -= 1
                    elif countShip < 7:
                        if (row + 1) >= 10:
                            printAttentionMessage()
                            countShip -= 1
                        elif (row + 1) < 10:
                            if self.checkDistance(position, row, col, 2) == False:
                                printAttentionMessage()
                                countShip -= 1
                    elif countShip < 9:
                        if (row + 2) >= 10:
                            printAttentionMessage()
                            countShip -= 1
                        elif (row + 2) < 10:
                            if self.checkDistance(position, row, col, 3) == False:
                                printAttentionMessage()
                                countShip -= 1
                                countDown += 1
                    elif countShip < 10:
                        if (row + 3) >= 10:
                            printAttentionMessage()
                            countShip -= 1
                        elif (row + 3) < 10:
                            if self.checkDistance(position, row, col, 4) == False:
                                printAttentionMessage()
                                countShip -= 1
                                countDown += 1
            elif countShip < 9:
                if (col + 2) >= 10:
                    printAttentionMessage()
                    countShip -= 1
                elif (col + 2) < 10:
                    if self.checkDistance(position, row, col, 3) == False:
                        printAttentionMessage()
                        countShip -= 1
                        countDown += 1
            elif countShip < 10:
                if (col + 3) >= 10:
                    printAttentionMessage()
                    countShip -= 1
                elif (col + 3) < 10:
                    if self.checkDistance(position, row, col, 4) == False:
                        printAttentionMessage()
                        countShip -= 1
                        countDown += 1
        countShip += 1
        if countShip >= 7 and countShip < 11:
            countDown -= 1

    def quitGame(self):
        """Method which quit from game, destroy window and close program."""
        # print("Function which quit from game!")
        self.__root.destroy()
        exit(0)

    def resetGame(self):
        """Method which clear all of the global variables."""
        # print("Function which reset game!")
        global countShip
        global rotateShip
        global planeNumber
        global countDown
        global playerScore
        global aiScore

        global playerShipPos
        global playerMiss
        global playerSpace
        global playerShot

        global aiShipPos
        global aiMiss
        global aiSpace
        global aiShot
        global startGame

        startGame = False

        countShip = 0
        rotateShip = 0
        planeNumber = 0
        countDown = 3

        playerShipPos = []
        aiShipPos = []

        aiMiss = []
        aiShot = []
        aiSpace = []

        playerMiss = []
        playerShot = []
        playerSpace = []

        for row in range(10):
            for col in range(10):
                self.__gridPlayer[row][col].configure(bg="silver", state=NORMAL, cursor="hand2", relief=SUNKEN)
                self.__gridAi[row][col].configure(bg="gray", state=NORMAL, cursor="hand2", relief=RAISED)

    def rotateShip(self):
        """Method which change the ship orientation."""
        # print("Function to change direction vertical/horizontal.")
        global rotateShip
        global countShip

        rotateShip += 1

    def checkDistance(self, position, row, col, times):
        """Method that check the ship distance from another one.
            :param position: co-odinates of ship beginning
            :param row: row number
            :param col: column number
            :param times: the size of ship."""
        # print("Function which check distance to ships!")
        check = []
        global playerSpace
        global playerShipPos

        if position == 1:
            for i in range(times):
                check.append((row + i, col))
            if (not [el for el in playerSpace if el in check]) and (not [el for el in playerShipPos if el in check]):
                for i in range(times):
                    playerShipPos.append((row + i, col))
                    self.__gridPlayer[row + i][col].configure(bg="black", state=DISABLED, cursor="left_ptr",
                                                              relief=SUNKEN)
                self.playerSpaceAroundShip(position, row, col, times)
                self.aiShip(times, times - 1)
            else:
                return False
        else:
            for i in range(times):
                check.append((row, col + i))
            if (not [el for el in playerSpace if el in check]) and (not [el for el in playerShipPos if el in check]):
                for i in range(times):
                    playerShipPos.append((row, col + i))
                    self.__gridPlayer[row][col + i].configure(bg="black", state=DISABLED, cursor="left_ptr",
                                                              relief=SUNKEN)
                self.playerSpaceAroundShip(position, row, col, times)
                self.aiShip(times, times - 1)
            else:
                return False

    def playerSpaceAroundShip(self, position, row, col, times):
        """Method assurance free space around player ship.
        Disables the button action around them.
        :param position: position of ship
        :param row: row number of ship
        :param col: column number of ship
        :param times: size of ship"""

        # print("Function which ensure free space around the ship!")
        global playerSpace

        if position == 1:
            for i in range(times):
                playerSpace = placeShip1(playerSpace, row, col, times, i)
        else:
            for i in range(times):
                playerSpace = placeShip3(playerSpace, row, col, times, i)
        tmp = []

        for i in range((len(playerSpace))):
            rows, cols = playerSpace[i]
            if (0 <= rows <= 9) and (0 <= cols <= 9):
                tmp.append((rows, cols))

        playerSpace = set(tmp)
        playerSpace = list(playerSpace)

        for i in playerSpace:
            rows, cols = i
            self.__gridPlayer[rows][cols].configure(state=DISABLED, cursor="left_ptr")

    def aiSpaceAroundShip(self, position, row, col, times, i):
        """Method that disables the possibility of clicking the buttons around the ship of AI.
        :param position: position of ship beginnings
        :param row: row number
        :param col: columns number
        :param times: size of ship
        :param i: size of ship in other axis"""
        # print("Function which ensure free space around the ship!")
        global aiSpace

        if (position == 1):
            aiSpace = placeShip1(aiSpace, row, col, times, i)
        else:
            aiSpace = placeShip3(aiSpace, row, col, times, i)

        aiSpace = set(aiSpace)
        aiSpace = list(aiSpace)

    def playerShotShip(self):
        """Method allowing the player to shot."""
        # print("Function that supports the user's shot!")
        global planeNumber
        if planeNumber < 100:
            row = randrange(10)
            col = randrange(10)
            if (row, col) not in playerShot:
                if (row, col) in playerShipPos:
                    self.__gridPlayer[row][col].configure(bg="red", state=DISABLED, cursor="left_ptr", relief=SUNKEN)
                    playerShot.append((row, col))
                    playerShipPos.remove((row, col))
                elif (row, col) not in playerMiss:
                    self.__gridPlayer[row][col].configure(bg="blue", state=DISABLED, cursor="left_ptr", relief=SUNKEN)
                    playerShot.append((row, col))
            else:
                self.playerShotShip()
        else:
            if messagebox.showinfo("End of Game", "Remis"):
                self.resetGame()

    def aiShotShip(self, row, col):
        """Method allowing the AI to shot."""
        # print("Function that supports the ai shot!")
        global countShip
        if countShip > 9:
            if (row, col) in aiShipPos:
                self.__gridAi[row][col].configure(bg="red", state=DISABLED, relief=SUNKEN)
                aiShot.append((row, col))
                aiShipPos.remove((row, col))
                return True

            elif (row, col) not in aiMiss:
                self.__gridAi[row][col].configure(bg="blue", state=DISABLED, relief=SUNKEN)
                aiMiss.append((row, col))
                return False

    def __init__(self, root):

        self.__root = root

        self.__buttonNewGame = Button(self.__root, text="New Game", height=2, width=10, bg="lightsteelblue",
                                      command=newGame)
        self.__buttonQuit = Button(self.__root, text="Quit", height=2, width=10, bg="lightsteelblue",
                                   command=lambda: self.quitGame())
        self.__buttonReset = Button(self.__root, text="Reset", height=2, width=10, bg='lightsteelblue',
                                    command=self.resetGame)
        self.__buttonRotate = Button(self.__root, text="Rotate", height=2, width=10, bg='lightsteelblue',
                                     command=self.rotateShip)

        self.__gridPlayer = [[0 for i in range(10)] for j in range(10)]
        self.__gridAi = [[0 for i in range(10)] for j in range(10)]

        for i in range(10):
            for j in range(10):
                self.__gridPlayer[i][j] = Button(self.__root, height=2, width=3, bg='silver',
                                                 command=lambda i=i, j=j: self.playerClick(i, j))
                self.__gridPlayer[i][j].grid(row=i + 3, column=j + 1)

        self.__textPlayerMap = Label(self.__root, height=3, width=63, text="Player Map")
        self.__textPlayerMap.grid(row=1, column=1, columnspan=10)

        self.__textAIMap = Label(self.__root, height=3, width=62, text='AI Map')
        self.__textAIMap.grid(row=1, column=13, columnspan=10)

        for i in range(10):
            for j in range(10):
                self.__gridAi[i][j] = Button(self.__root, height=2, width=3, bg='grey',
                                             command=lambda i=i, j=j: self.aiClick(i, j))
                self.__gridAi[i][j].grid(row=i + 3, column=j + 13)

        self.__root.grid_columnconfigure(11, minsize=22)
        self.__buttonNewGame.grid(row=3, column=25, columnspan=2)
        self.__buttonReset.grid(row=5, column=25, columnspan=2)
        self.__buttonRotate.grid(row=7, column=25, columnspan=2)
        self.__buttonQuit.grid(row=9, column=25, columnspan=2)


# Program Start :)
root = Tk()
root.title("BattleShip")
game = StartGame(root=root)
root.mainloop()
