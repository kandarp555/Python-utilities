board = ["-" for x in range(10)]
def display_board():
    for i in range(1,len(board),3):
        for j in range(i,i+3):
            print(board[j],end = ' ')
        print()   
def win_lose(player):
    if(board[1]==board[2]==board[3]==player or 
        board[4]==board[5]==board[6]==player or
        board[7]==board[8]==board[9]==player or
        board[1]==board[4]==board[7]==player or 
        board[2]==board[5]==board[8]==player or
        board[2]==board[6]==board[9]==player or 
        board[1]==board[5]==board[9]==player or
        board[3]==board[5]==board[7]==player):
        return True
    else:
        return False
def board_full():
    for i in range(1,10):
        if board[i]=="-":
            return False
    return True
def play_game():
    player = "x"
    while not win_lose("x") and not win_lose("o") and not board_full():
        display_board()
        if player == "o":
            choice = int(input("\nPlayer-2, Enter number from 1 to 9 to place your sign:\n"))
        else:   
            choice = int(input("\nPlayer-1, Enter a number from 1 to 9 to place your sign:\n"))
        if board[choice]=="-":
            board[choice] = player
            if player == "x":
                player = "o"
            else:
                player = "x"
        else:
            print("That space is already taken. Please choose another.")
    display_board()
    if win_lose("x"):
        print("\nx Wins!")
    elif win_lose("o"):
        print("\no wins!")
    else:
        print("\nIt's a tie!")
play_game()

