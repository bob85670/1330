board = [["0", "1", "2"], 
         ["3", "4", "5"], 
         ["6", "7", "8"]]

def print_board():
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end='')
        print()
    
def update_board(val, cur):
    i = val // 3
    j = val % 3
    board[i][j] = cur
    
def check_win_condition(cur):
    # Check rows
    for row in board:
        if all(cell == cur for cell in row):
            return True
            
    # Check columns
    for col in range(3):
        if all(board[row][col] == cur for row in range(3)):
            return True
            
    # Check diagonals
    if all(board[i][i] == cur for i in range(3)):
        return True
    if all(board[i][2-i] == cur for i in range(3)):
        return True
        
    return False

def main():
    for i in range(9):
        print_board()
        if i % 2 == 0:
            curPlayer = "X"
            val = int(input(("X--> ")))
        else:
            curPlayer = "O"
            val = int(input(("O--> ")))
        update_board(val, curPlayer)
        if check_win_condition(curPlayer):
            print("Winner: " + curPlayer)
            return
    print("Winner: None")

if __name__ == "__main__":
    main()