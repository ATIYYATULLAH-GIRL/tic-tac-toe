the_Board={"7":" ","8":" ","9":" ","4":" ","5":" ","6":" ","1":" ","2":" ","3":" "}
board_keys=[]
def printBoard(board):
    print(board["7"]+"|"+board["8"]+"|"+board["9"])
    print("-+-+-")
    print(board["4"]+"|"+board["5"]+"|"+board["6"])
    print("-+-+-")
    print(board["1"]+"|"+board["2"]+"|"+board["3"])
    print("-+-+-")
def game():
    turn="X"
    count=0
    for i in range(10):
        printBoard(the_Board)
        print("It is your turn"+turn+ "Move to which place")
        move=input()
        if the_Board[move]==" ":
            the_Board[move]=turn
            count+=1
        else:
            print("It is already filled")
            continue
        if count>=5:
            if the_Board["7"]==the_Board["8"]==the_Board==["9"]!=" ":
                printBoard(the_Board)
                print("Game Over",turn,"won")
                break
            elif the_Board["4"]==the_Board["5"]==the_Board==["6"]!=" ":
                printBoard(the_Board)
                print("Game Over",turn,"won")
                break
            elif the_Board["1"]==the_Board["2"]==the_Board==["3"]!=" ":
                printBoard(the_Board)
                print("Game Over",turn,"won")
                break
            elif the_Board["1"]==the_Board["4"]==the_Board==["7"]!=" ":
                printBoard(the_Board)
                print("Game Over",turn,"won")
                break
            elif the_Board["2"]==the_Board["5"]==the_Board==["8"]!=" ":
                printBoard(the_Board)
                print("Game Over",turn,"won")
                break
            elif the_Board["3"]==the_Board["6"]==the_Board==["9"]!=" ":
                printBoard(the_Board)
                print("Game Over",turn,"won")
                break
            elif the_Board["1"]==the_Board["5"]==the_Board==["9"]!=" ":
                printBoard(the_Board)
                print("Game Over",turn,"won")
                break
            elif the_Board["3"]==the_Board["5"]==the_Board==["7"]!=" ":
                printBoard(the_Board)
                print("Game Over",turn,"won")
                break
        if count==9:
            print("Game Over, its a TIE!!!")
        if turn=="X":
            turn="O"
        else:
            turn=="X"
    restart=input("Do you want to play again,(yes/no")
    if restart.lower()=="y":
        for key in board_keys:
            the_Board[key]=" "
        game()
if __name__=="__main__":
    game()