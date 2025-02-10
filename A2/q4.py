def create_board(size):
    board = []
    val = 0
    for i in range(size):
        row = []
        for j in range(size):
            row.append(val)
            val += 1
        board.append(row)
    return board


def print_board(board):
    largest = 0
    for row in board:
        for cell in row:
            if isinstance(cell, int):
                largest = max(largest, cell)
    
    digit = len(str(largest))
    
    for row in board:
        for cell in row:
            if isinstance(cell, str): 
                print(f"{cell:>{digit}}", end=" ")
            else: 
                print(f"{cell:>{digit}}", end=" ")
        print()

def update_board(val, cur, size, board):
    i = val // size
    j = val % size
    board[i][j] = cur
    
def check_win_condition(cur, size, board):
    # Check rows
    for row in board:
        if all(cell == cur for cell in row):
            return True
            
    # Check columns
    for col in range(size):
        if all(board[row][col] == cur for row in range(size)):
            return True
            
    # Check diagonals
    if all(board[i][i] == cur for i in range(size)):
        return True
    if all(board[i][size-1-i] == cur for i in range(size)):
        return True
        
    return False

def main():
    size = int(input("size--> "))
    board = create_board(size)

    for i in range(size ** 2):
        print_board(board)
        if i % 2 == 0:
            curPlayer = "X"
            val = int(input(("X--> ")))
        else:
            curPlayer = "O"
            val = int(input(("O--> ")))
        update_board(val, curPlayer, size, board)
        if check_win_condition(curPlayer, size, board):
            print("Winner: " + curPlayer)
            return
    print("Winner: None")

if __name__ == "__main__":
    main()