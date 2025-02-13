def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()

def remove_queen_attack_cell(board, x, y, n):
    # Mark horizontal line
    for i in range(n):
        board[x - 1][i] = 1
    
    # Mark vertical line
    for j in range(n):
        board[j][y - 1] = 1

    # diagonal top-left to bottom-right
    i, j = x - 1, y - 1
    while i >= 0 and j >= 0:
        board[i][j] = 1
        i -= 1
        j -= 1
    i, j = x, y
    while i < n and j < n:
        board[i][j] = 1
        i += 1
        j += 1
    
    # anti-diagonal top-right to bottom-left
    i, j = x - 1, y - 1
    while i >= 0 and j < n:
        board[i][j] = 1
        i -= 1
        j += 1
    i, j = x - 1, y - 1
    while i < n and j >= 0:
        board[i][j] = 1
        i += 1
        j -= 1

def calculate_free_cells(n, board):
    print_board(board)
    cells = n ** 2
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cells -= 1
    return cells

def main():
    n, m = map(int, input().split())
    board = [[0 for j in range(n)] for i in range(n)]
    for i in range(m):
        x, y = map(int, input().split())
        remove_queen_attack_cell(board, x, y, n)
    space = calculate_free_cells(n, board)
    return space


if __name__ == "__main__":
    print(main())