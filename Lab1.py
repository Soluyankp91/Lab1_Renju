ROW_LENGTH = 19
COL_LENGTH = 19
WINNING_LENGTH = 5
BLACK_STONE_NUMBER = 1
WHITE_STONE_NUMBER = 2

def check_horizontal(board, row, col, color):
    count = 1
    for i in range(1, WINNING_LENGTH):
        if col + i < COL_LENGTH and board[row][col + i] == color:
            count += 1
        else:
            break
    if count == WINNING_LENGTH:
        if (col + WINNING_LENGTH < COL_LENGTH and board[row][col + WINNING_LENGTH] == color) or (col > 0 and board[row][col - 1] == color):
            return 0, None  # More than five consecutive stones
    return count, (row, col)

def check_vertical(board, row, col, color):
    count = 1
    for i in range(1, WINNING_LENGTH):
        if row + i < ROW_LENGTH and board[row + i][col] == color:
            count += 1
        else:
            break
    if count == WINNING_LENGTH:
        if (row + WINNING_LENGTH < ROW_LENGTH and board[row + WINNING_LENGTH][col] == color) or (row > 0 and board[row - 1][col] == color):
            return 0, None  # More than five consecutive stones
    return count, (row, col)

def check_diagonal_top_left_bottom_right(board, row, col, color):
    count = 1
    for i in range(1, WINNING_LENGTH):
        if row + i < ROW_LENGTH and col + i < COL_LENGTH and board[row + i][col + i] == color:
            count += 1
        else:
            break
    if count == WINNING_LENGTH:
        if (row + WINNING_LENGTH < ROW_LENGTH and col + WINNING_LENGTH < COL_LENGTH and board[row + WINNING_LENGTH][col + WINNING_LENGTH] == color) or (row > 0 and col > 0 and board[row - 1][col - 1] == color):
            return 0, None  # More than five consecutive stones
    return count, (row, col)

def check_diagonal_bottom_left_top_right(board, row, col, color):
    count = 1
    for i in range(1, WINNING_LENGTH):
        if row + i < ROW_LENGTH and col - i >= 0 and board[row + i][col - i] == color:
            count += 1
        else:
            break
    if count == WINNING_LENGTH:
        if (row + WINNING_LENGTH < ROW_LENGTH and col - WINNING_LENGTH >= 0 and board[row + WINNING_LENGTH][col - WINNING_LENGTH] == color) or (row > 0 and col < COL_LENGTH - 1 and board[row - 1][col + 1] == color):
            return 0, None  # More than five consecutive stones
    return count, (row + (count - 1), col - (count - 1))

def check_winning_lane(board, row, col):
    color = board[row][col]

    for check in [check_horizontal, check_vertical, check_diagonal_top_left_bottom_right, check_diagonal_bottom_left_top_right]:
        count, start_pos = check(board, row, col, color)
        if count == WINNING_LENGTH:
            return True, start_pos

    return False, None

def check_winner(board):
    for row in range(ROW_LENGTH):
        for col in range(COL_LENGTH):
            if board[row][col] != 0:
                win, start_pos = check_winning_lane(board, row, col)
                if win:
                    return (BLACK_STONE_NUMBER if board[row][col] == BLACK_STONE_NUMBER else WHITE_STONE_NUMBER), start_pos
    return 0, None

def main():
    try:
        with open('data.txt', 'r') as file:
            count = int(file.readline())
            if count < 1 or count > 11:
                print("Number of test cases is out of valid range (1-11)")
                return
            for num_test_cases in range(count):
                array = []
                for line in range(19):
                    row = [int(num) for num in file.readline().strip()]
                    array.append(row)
                winner, win_pos = check_winner(array)
                print(winner)
                if winner != 0:
                    print(win_pos[0] + 1, win_pos[1] + 1)
    except ValueError:
        print('Wrong input file')
        return
    except IndexError:
        print('Wrong game`s field size ')
        return

if __name__ == "__main__":
    main()
