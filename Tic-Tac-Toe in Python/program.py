from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import numpy as np
import random as rand

# varijable-brojači pobjeda
pWins = 0
cWins = 0

class grid:
    # klasa 2d polja za praćenje igre, uz pomoć te klase radimo virualno polje
    grid = np.zeros([3, 3])
    
def checkWinner(board): # provjeravamo ako su tri jedinice u istom redu, stupcu ili dijagonale
    if board.grid[0][0] == 1 and board.grid[0][1] == 1 and board.grid[0][2] == 1:
        return 1
    if board.grid[1][0] == 1 and board.grid[1][1] == 1 and board.grid[1][2] == 1:
        return 1
    if board.grid[2][0] == 1 and board.grid[2][1] == 1 and board.grid[2][2] == 1:
        return 1
    if board.grid[0][0] == 1 and board.grid[1][0] == 1 and board.grid[2][0] == 1:
        return 1
    if board.grid[0][1] == 1 and board.grid[1][1] == 1 and board.grid[2][1] == 1:
        return 1
    if board.grid[0][2] == 1 and board.grid[1][2] == 1 and board.grid[2][2] == 1:
        return 1
    if board.grid[0][0] == 1 and board.grid[1][1] == 1 and board.grid[2][2] == 1:
        return 1
    if board.grid[2][0] == 1 and board.grid[1][1] == 1 and board.grid[0][2] == 1:
        return 1
    
    if board.grid[0][0] == -1 and board.grid[0][1] == -1 and board.grid[0][2] == -1:
        return -1
    if board.grid[1][0] == -1 and board.grid[1][1] == -1 and board.grid[1][2] == -1:
        return -1
    if board.grid[2][0] == -1 and board.grid[2][1] == -1 and board.grid[2][2] == -1:
        return -1
    if board.grid[0][0] == -1 and board.grid[1][0] == -1 and board.grid[2][0] == -1:
        return -1
    if board.grid[0][1] == -1 and board.grid[1][1] == -1 and board.grid[2][1] == -1:
        return -1
    if board.grid[0][2] == -1 and board.grid[1][2] == -1 and board.grid[2][2] == -1:
        return -1
    if board.grid[0][0] == -1 and board.grid[1][1] == -1 and board.grid[2][2] == -1:
        return -1
    if board.grid[2][0] == -1 and board.grid[1][1] == -1 and board.grid[0][2] == -1:
        return -1
        
    
def compChoice(board): #računalo odabire indexe polja 
    
    while 1:
        # slučajni odabir indeksa polja
        x = rand.randint(0, 2) 
        y = rand.randint(0, 2)
        
        # brojač za provjeru ako su sva polja već popunjena, u suprotnome while petlja ide u beskonačno
        isFullCounter = 0 
        
        # provjera popunjenosti
        for i in range(3):
            for j in range(3):
                if board.grid[i][j] != 0:
                    isFullCounter = isFullCounter + 1 
       
        # ukoliko brojač dođe do 9, to znači da su sva polja popunjena, pa je moguće da je rezultat izjednačen, ali potrebne su daljnje provjere, povratna vrijednost je -1
        if isFullCounter == 9: 
            isFullCounter = 0
            return (10, 0)
        
        # ukoliko računalo odabere indekse polja gdje odabira još nema, funkcija vraća indekse polja koja treba popuniti
        if board.grid[x, y] == 0:    
            isFullCounter = 0
            return (x, y)
        
def choice(buttons, board, x, y, playerWins, computerWins):
    
    # korištenjem riječi global, možemo mijenjati varijable unutar funkcije
    global pWins
    global cWins
    
    # nakon korisnikovog odabira, određeno se polje popunjava znakom "X", a samom gumbu mijenjamo stanje u "disabled", čime smo onemogućili ponovni njegov odabir
    buttons[x][y].config(text="X")
    buttons[x][y]["state"] = "disabled"
    board.grid[x, y] = 1
    
    # dohvat koordinata koje je računalo izabralo
    i, j = compChoice(board)
    
    # provjera ako je korisnik pobjednik
    winner = checkWinner(board)
    if winner == 1:
        messagebox.showinfo(title="Outcome", message="You are the WINNER!")
        pWins += 1
        pwText = "Player wins: " + str(pWins)
        playerWins.config(text=pwText)
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(text="")
                buttons[i][j]["state"] = "normal"
                board.grid[i][j] = 0
        return
    
    # provjera ako je došlo do nerješenog rezultata
    if i == 10:
        messagebox.showinfo(title="Outcome", message="It's a DRAW!")
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(text="")
                buttons[i][j]["state"] = "normal"
                board.grid[i][j] = 0
                
        return
    
    # nakon odabira računala, određeno se polje popunjava znakom "0",  a samom gumbu mijenjamo stanje u "disabled", čime smo onemogućili ponovni njegov odabir
    # print funkcije služe samo za praćenje stanja igre u konzoli
    print(board.grid)
    board.grid[i][j] = -1
    buttons[i][j].config(text="O")
    buttons[i][j]["state"] = "disabled"
    print(board.grid)
    
    #provjera ako je računalo pobjednik
    winner = checkWinner(board)
    if winner == -1:
        messagebox.showinfo(title="Outcome", message="*Sigh...* The computer is the WINNER!")
        cWins += 1
        cwText = "Computer wins: " + str(cWins)
        computerWins.config(text=cwText)
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(text="")
                buttons[i][j]["state"] = "normal"
                board.grid[i][j] = 0
        return
  
def game():
    # inicijalizacija prozora za igru
    game = Tk()
    game.title("WELCOME TO TIC-TAC-TOE")
    game.geometry("655x338")
    game.configure(bg='dark blue')
    
    # stvaranje objekta klase grid, ovo nam je potrebno za provjeru popunjenosti 2d polja
    board = grid()
    
    turnLabel = Label(game, text = "Click on any available piece!", width=30, height=2)
    turnLabel.place(x=375, y=100)
    playerWins = Label(game, text = "Player wins: 0", width=30, height=2)
    playerWins.place(x=375, y=165)
    computerWins = Label(game, text = "Computer wins: 0", width=30, height=2)
    computerWins.place(x=375, y=215)
    
    # stvaranje gumba za 2d igraće polje, gumbima se dodaju "onclick" funkcije
    buttons = [[None for x in range(3)] for y in range(3)]
    
    buttons[0][0] = Button(game, text = "", height=6, width=12, bd=8)
    buttons[0][1] = Button(game, text = "", height=6, width=12, bd=8)
    buttons[0][2] = Button(game, text = "", height=6, width=12, bd=8)
    buttons[1][0] = Button(game, text = "", height=6, width=12, bd=8)
    buttons[1][1] = Button(game, text = "", height=6, width=12, bd=8)
    buttons[1][2] = Button(game, text = "", height=6, width=12, bd=8)
    buttons[2][0] = Button(game, text = "", height=6, width=12, bd=8)
    buttons[2][1] = Button(game, text = "", height=6, width=12, bd=8)
    buttons[2][2] = Button(game, text = "", height=6, width=12, bd=8)
            
    buttons[0][0].configure(command=lambda: choice(buttons, board, 0, 0, playerWins, computerWins))
    buttons[0][1].configure(command=lambda: choice(buttons, board, 0, 1, playerWins, computerWins))
    buttons[0][2].configure(command=lambda: choice(buttons, board, 0, 2, playerWins, computerWins))
    buttons[1][0].configure(command=lambda: choice(buttons, board, 1, 0, playerWins, computerWins))
    buttons[1][1].configure(command=lambda: choice(buttons, board, 1, 1, playerWins, computerWins))
    buttons[1][2].configure(command=lambda: choice(buttons, board, 1, 2, playerWins, computerWins))
    buttons[2][0].configure(command=lambda: choice(buttons, board, 2, 0, playerWins, computerWins))
    buttons[2][1].configure(command=lambda: choice(buttons, board, 2, 1, playerWins, computerWins))
    buttons[2][2].configure(command=lambda: choice(buttons, board, 2, 2, playerWins, computerWins))     

    buttons[0][0].grid(column=0, row=0)
    buttons[0][1].grid(column=1, row=0)   
    buttons[0][2].grid(column=2, row=0)
    buttons[1][0].grid(column=0, row=1)
    buttons[1][1].grid(column=1, row=1)
    buttons[1][2].grid(column=2, row=1)
    buttons[2][0].grid(column=0, row=2)
    buttons[2][1].grid(column=1, row=2)
    buttons[2][2].grid(column=2, row=2)       
    
    game.mainloop()

def start():
    # inicijalizija i postavljanje početnog prozora
    startGame = Tk()
    startGame.title("Tic - Tac - Toe")
    startGame.geometry("655x330")
    
    myFont = font.Font(family='Courier', size=20, weight='bold')
    
    playerBtn = Button(startGame, text="PRESS TO START", height=10, width=43, bg="dark blue",
                             fg="white", activebackground="White", activeforeground="red",
                             command=game)
    
    playerBtn['font'] = myFont
    
    playerBtn.grid(column=0, row=0)
    
    startGame.mainloop() 

#da znamo od koje funkcije kreće, drugim riječima definiramo našu main funkciju
if __name__ == '__main__':
    start()
