from tkinter import *
from tkinter import messagebox
from Const import *

class StartGame(object):
    """Klasa realizujaca całość pracy programu."""

    def printAttentionMessage(self):
        # print("Method which print information about the wrong placing of the ship!")
        messagebox.showwarning("Warning", "Ustaw statek zgodnie z zasadami!!!")

    def aiClick(self):
        # print("Ai put ship!")
        pass

    def playerClick(self, row, col):
        # print("Player put ship!")
        global countShip
        global rotateShip
        global countDown
        global playerSpace

        position = rotateShip % 2

        if ( position == 1):
            if(countShip < 4):
                if(self.checkDistance(position, row, col, 1) == False):
                    self.printAttentionMessage()
                    countShip -= 1
            elif(countShip < 7):
                if((row+1 >= 10)):
                    self.printAttentionMessage()
                    countShip -= 1
                elif(row+1) < 10:
                    if(self.checkDistance(position, row, col, 2) == False):
                        self.printAttentionMessage()
                        countShip -= 1
            elif(countShip < 9):
                if((row + 2) >= 10):
                    self.printAttentionMessage()
                    countShip -= 1
                elif(row+2) < 10:
                    if(self.checkDistance(position, row, col, 3) == False):
                        self.printAttentionMessage()
                        countShip -= 1
                        countDown += 1
            elif(countShip < 10):
                if ((row + 3) >= 10):
                    self.printAttentionMessage()
                    countShip -= 1
                elif(row + 3) < 10:
                    if(self.checkDistance(position, row, col, 4) == False):
                        self.printAttentionMessage()
                        countShip -= 1
                        countDown += 1
        else:
            if( countShip < 4):
                if(self.checkDistance(position, row, col, 1) == False):
                    self.printAttentionMessage()
                    countShip -= 1
            elif( countShip < 7):
                if((col + 1) >= 10):
                    self.printAttentionMessage()
                    countShip -= 1
                elif(col + 1) < 10:
                    if(self.checkDistance(position, row, col, 2) == False):
                        self.printAttentionMessage()
                        countShip -= 1
            elif(countShip < 9):
                    if ((col+2)>=10):
                        self.printAttentionMessage()
                        countShip -= 1
                    elif(col+2)<10:
                         if (self.checkDistance(position, row, col, 3)==False):
                              self.printAttentionMessage()
                              countShip -= 1
                              countDown += 1
            elif(countShip < 10):
                if ((col+3)>=10):
                    self.printAttentionMessage()
                    countShip -= 1
                elif(col+3)<10:
                     if (self.checkDistance(position, row, col, 4)==False):
                          self.printAttentionMessage()
                          countShip -= 1
                          countDown += 1
        countShip += 1
        if(countShip >= 7 and countShip < 11):
              countDown -=1


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
        global rotateShip
        global countShip

        rotateShip += 1

    def checkDistance(self, position, row, col, times):
        # print("Function which check distance to ships!")
        check_list =[]
        global playerSpace
        global playerShipPos

        if (position == 1):
              for i in range(times):
                   check_list.append((row+i,col))
              if((not[el for el in playerSpace if el in check_list]) and (not[el for el in playerShipPos if el in check_list])):
                   for i in range(times):
                        playerShipPos.append((row + i, col))
                        self.gridPlayer[row+i][col].configure(bg="black", state=DISABLED, cursor="left_ptr", relief=SUNKEN)
                   self.playerSpaceAroundShip(position, row, col, times)
                   self.aiShotShip(times,times-1)
              else:
                   return False
        else:
              for i in range(times):
                   check_list.append((row,col+i))
              if (not[el for el in playerSpace if el in check_list]) and (not[el for el in playerShipPos if el in check_list]):
                   for i in range(times):
                        playerShipPos.append((row, col + i))
                        self.gridPlayer[row][col+i].configure(bg="black", state=DISABLED, cursor="left_ptr", relief=SUNKEN)
                   self.playerSpaceAroundShip(position, row, col, times)
                   self.aiShotShip(times, times-1)
              else:
                   return False

    def placeShip1(self, x, row, col, times, i):
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

    def placeShip3(self, x, row, col, times, i):
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


    def playerSpaceAroundShip(self, position, row, col, times):
        # print("Function which ensure free space around the ship!")
        global playerSpace

        if (position == 1):
          for i in range(times):
                playerSpace = self.placeShip1(playerSpace, row, col, times, i)
        else:
          for i in range(times):
                playerSpace = self.placeShip3(playerSpace, row, col, times, i)
        tmp=[]

        for i in range((len(playerSpace))):
          rows,cols = playerSpace[i]
          if((rows >= 0 and rows <= 9) and (cols >= 0 and cols <= 9)):
               tmp.append((rows,cols))

        playerSpace = set(tmp)
        playerSpace = list(playerSpace)

        for i in playerSpace:
          rows,cols = i
          self.button_player[rows][cols].configure(state=DISABLED, cursor="left_ptr")

    def aiSpaceAroundShip(self, position, row, col, times, i):
        # print("Function which ensure free space around the ship!")
        global aiSpace

        if (position == 1):
            aiSpace = self.placeShip1(aiSpace, row, col, times, i)
        else:
            aiSpace = self.placeShip3(aiSpace, row, col, times, i)

        aiSpace = set(aiSpace)
        aiSpace = list(aiSpace)

    def playerShotShip(self):
        # print("Function that supports the user's shot!")
        pass

    def aiShotShip(self):
        # print("Function that supports the ai shot!")
        pass

    def getWinner(self):
        # print("Function that checks the win condition!")
        global aiShipPos
        global playerShipPos

        if ((len(aiShipPos) == 0) and (countShip >= 10)):
            messagebox.showinfo("", "Wygrana!")
        elif ((len(playerShipPos) == 0) and (countShip >= 10)):
             messagebox.showinfo("", "Przegrana!")



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
