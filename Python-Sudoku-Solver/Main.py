board = [                                                                       # Board to be solved
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
board2 = [                                                                       # Bad Board
    [7,8,1,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,4,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_Board(board):                                                         # Defining printBoard with array parameter
    for i in range(len(board)):                                                 # Iterating through row                 
        if i % 3 == 0 and i != 0:                                               # If row modulo 3 is not equal to 0 or i is not 0
            print("---------------------------")                                # Print row divider

        for j in range(len(board[0])):                                          # Iterating thrpugh column
            if j % 3 == 0 and j != 0:                                           # If column modulo 3 is not equal to 0 or i is not 0
                print(" | ", end="")                                            # Print column divider without a '\n' 

            if j == 8:                                                          # Checking to see if iteration is at last line of the board
                print(board[i][j])                                              # Print number at row and column
            else:
                print(str(board[i][j]) + " ", end="")


def find_Empty_Space(board):                                                    # Defining function to find empty or spaces with zero
    for i in range(len(board)):                                                 # Iterating Through Row
        for j in range(len(board[0])):                                          # Iterating Through Column
            if board[i][j] == 0:                                                # If i and j = 0
                return (i, j)                                                   # Return empty or 0 to be solved for                                                 

    return None                                                                 # Return none if nothing found

def valid_Number(board, number, position):                                      # Define valid number with 3 parameters
    for i in range(len(board[0])):                                              # Iterating Through Row
        if board[position[0]][i] == number and position[1] != i:                # If number equals number in same row
            return False                                                        # Return false if not a vaild number

 
    for i in range(len(board)):                                                 # Iterating Through Column
        if board[i][position[1]] == number and position[0] != i:                # If number equals number in same column
            return False                                                        # Return false if not a vaild number

    box_x = position[1] // 3                                                    # Box variable for row
    box_y = position[0] // 3                                                    # Box variable for column

    for i in range(box_y * 3, box_y * 3 + 3):                                   # Iterating Through Row in box
        for j in range(box_x * 3, box_x * 3 + 3):                               # Iterating Through Column in box 
            if board[i][j] == number and (i,j) != position:                     # If numbers matches
                return False                                                    # Return false if not a vaild number

    return True                                                                 # Return True if a vaild number

def solve_Board(board):                                                         # Define solution for board
    find = find_Empty_Space(board)                                              # Call function for empty space into variable find
    if not find:                                                                # If not find or last number for solved board
        return True                                                             # Return solved board
    else:
        row, column = find                                                      # Find return position of i and j

    for i in range(1,10):                                                       # Iterating Through numbers 1 through 9
        if valid_Number(board, i, (row, column)):                               # If right number, insert number into board 
            board[row][column] = i                                              # If right number, insert number into board

            if solve_Board(board):                                              # Recursively call solve function
                return True                                                     # Return solved board

            board[row][column] = 0                                              # If not solved reset number at position i and j to 0
            
    return False                                                                # Return false for no solution

print("\nSudoku Board Before Solution")
print("---------------------------")
print_Board(board)
print("---------------------------")
solve_Board(board)
print("\nSudoku Board After Solution ")
print("---------------------------")
print_Board(board)