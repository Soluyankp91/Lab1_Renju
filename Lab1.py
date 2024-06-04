ROW_LENGTH = 19
COL_LENGTH = 19
WINNING_LENGTH = 5
BLACK_STONE_NUMBER = 1
WHITE_STONE_NUMBER = 2

def check_horizontal(board, row, col, color):
    if(col + WINNING_LENGTH > ROW_LENGTH):
      return 0, None
    count = 1
    for i in range(1, WINNING_LENGTH):
        if col + i >= COL_LENGTH or board[row][col + i] != color:
            break;
        count+=1

    if count == WINNING_LENGTH:
      has_right_extra_stone = (
        col + WINNING_LENGTH < COL_LENGTH and 
        board[row][col + WINNING_LENGTH] == color
      )
    
      has_left_extra_stone = (
        col > 0 and 
        board[row][col - 1] == color
      )
    
      if has_right_extra_stone or has_left_extra_stone:
        return 0, None

    return count, (row, col)

def check_vertical(board, row, col, color):
    if(row + WINNING_LENGTH > ROW_LENGTH):
      return 0, None
    count = 1
    for i in range(1, WINNING_LENGTH):
        if row + i >= ROW_LENGTH or board[row + i][col] != color:
            break;
        count += 1

    if count == WINNING_LENGTH:

      has_bottom_extra_stone = (
        row + WINNING_LENGTH < ROW_LENGTH and 
        board[row + WINNING_LENGTH][col] == color
      )
    
      has_top_extra_stone = (
        row > 0 and 
        board[row - 1][col] == color
      )
    
      if has_bottom_extra_stone or has_top_extra_stone:
        return 0, None

    return count, (row, col)

def check_diagonal_top_left_bottom_right(board, row, col, color):
    if(row + WINNING_LENGTH > ROW_LENGTH or col + WINNING_LENGTH > ROW_LENGTH):
      return 0, None
    count = 1
    for i in range(1, WINNING_LENGTH):
        if row + i >= ROW_LENGTH or col + i >= COL_LENGTH or board[row + i][col + i] != color:
            break;
        count += 1
    if count == WINNING_LENGTH:

      has_bottom_right_extra_stone = (
        row + WINNING_LENGTH < ROW_LENGTH and 
        col + WINNING_LENGTH < COL_LENGTH and 
        board[row + WINNING_LENGTH][col + WINNING_LENGTH] == color
      )
    
      has_top_left_extra_stone = (
        row > 0 and 
        col > 0 and 
        board[row - 1][col - 1] == color
      )
    
      if has_bottom_right_extra_stone or has_top_left_extra_stone:
        return 0, None
    return count, (row, col)

def check_diagonal_bottom_left_top_right(board, row, col, color):
    if(row + WINNING_LENGTH > ROW_LENGTH or col - WINNING_LENGTH < -1):
      return 0, None
    count = 1

    for i in range(1, WINNING_LENGTH):
        if row + i >= ROW_LENGTH or col - i < 0 or board[row + i][col - i] != color:
            break;
        count += 1

    if count == WINNING_LENGTH:
      has_bottom_left_extra_stone = (
        row + WINNING_LENGTH < ROW_LENGTH and 
        col - WINNING_LENGTH >= 0 and 
        board[row + WINNING_LENGTH][col - WINNING_LENGTH] == color
      )
    
      has_top_right_extra_stone = (
        row > 0 and 
        col < COL_LENGTH - 1 and 
        board[row - 1][col + 1] == color
      )
    
      if has_bottom_left_extra_stone or has_top_right_extra_stone:
        return 0, None
        
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
                for line in range(ROW_LENGTH):
                    row = [int(num) for num in file.readline().strip()]
                    array.append(row)
                # Validate board size
                if len(array) != ROW_LENGTH or any(len(row) != ROW_LENGTH for row in array):
                    print('Wrong game`s field size')
                    return
                if any(cell not in [0, 1, 2] for row in array for cell in row):
                    print('Invalid value in the game field')
                    return
                winner, win_pos = check_winner(array)
                print(winner)
                if winner != 0:
                    print(win_pos[0] + 1, win_pos[1] + 1)
    except ValueError:
        print('Wrong input file')
        return
    except IndexError:
        print('Wrong game`s field size')
        return

if __name__ == "__main__":
    main()
