import random
import os

# The following are constants.  A constant is a variable whose value does not
# change. We can use these constants anywhere in this module.

MIN_SHIP_SIZE = 1
MAX_SHIP_SIZE = 10
MAX_BOARD_SIZE = 10
UNKNOWN = '-'
EMPTY = '.'
HIT = 'X'
MISS = 'M'

# ===================== Helper Functions =====================

# Here is a helper function that we have written and used elsewhere in the
# supplied starter code.  You may make use of this function in the function(s) 
# that you write.

def in_bounds(row, col, board_size):
    """ (int, int, int) -> bool

    Return True if row and col are between 0 (inclusive) and board_size 
    (non-inclusive).
    
    >>> in_bounds(2, 9, 10)
    True
    >>> in_bounds(2, 9, 9)
    False
    """
    
    return 0 <= row < board_size and 0 <= col < board_size

# Add any helper functions that you write below.


# ===================== Required Functions =====================


# For make_move(), we have given you the required function header and docstring,
# and have supplied suggestions for reading moves and printing an error message.
# Complete the function body.
def make_move(view_board):
    """ (list of list of str) -> list of int

    Return a list containing a valid row and column for view_board.
    """

    # Uncomment and use this statement as many times as needed for input:
    [row, col] = get_move_from_player()
    if in_bounds(row, col, boardsize):
        return [row, col]
    # Uncomment and use this statement as many times as needed for output:
    else:
        print('Invalid move!')

    # Besides what is given above, do not use print or input anywhere else
    # in this function.



# Complete the other required functions before completing verify_symbol_board().
# For verify_symbol_board(), we have given you the header, the start of the 
# docstring, and a function body that always returns True.  This will allow you
# to play the game with valid game boards.  You need to complete the docstring 
# and replace the given function body with a correct function body, so that 
# invalid symbol boards are detected.

def verify_symbol_board(board, ships, sizes):
    """ (list of list of str, list of str, list of int) -> bool

    Preconditions: len(ships) == len(sizes) and len(ships) > 0,
                    board != [] and each row in board has length len(board).
                    
    """

    return True


# ========= Some functions that are called to play the game follow. ======
# ========= You may find it helpful to read and understand all of   ======
# ========= the code below these lines.  Do NOT change any of it!   ======

def display_boards(view_board, symbol_board):
    """ (list of list of str, list of list of str) -> NoneType

    Display the view_board and the symbol_board that belong to a player.
    """

    print()
    print('My view board.               My symbol board.')
    print()
    gap_between_boards = ' ' * (28 - len(view_board))
    # Display the column numbers
    print(' ', end='')
    for col in range(len(view_board)):
        print(col, end='')
    print(gap_between_boards + ' ', end='')
    for col in range(len(view_board)):
        print(col, end='')
    print()

    # Display row numbers and cell contents.
    for row in range(len(view_board)):
        print(row, end='')
        for col in range(len(view_board)):
            print(view_board[row][col], end='')
        print(gap_between_boards + str(row), end='')
        for col in range(len(symbol_board)):
            print(symbol_board[row][col], end='')
        print()

    print()
    print(' ' + HIT + ' means hit,                Upper-case means hit.')
    print('  ' + MISS + ' means miss.')

def get_move_from_player():
    """ () -> list of int

    Return a two item list that contains the player's move, or [-1,-1] if
    the player entered a move that cannot be interpreted.
    """

    row = input('Please enter the row: ')
    col = input('Please enter the column: ')

    if row.isdigit() and col.isdigit():
        return [int(row), int(col)]
    else:
        return [-1, -1]

def get_ship_labels(game_file):
    """ (file open for reading) -> list of str

    Return the ship labels that are found in game_file, a file that is open 
    for reading.
    """

    return game_file.readline().split()

def get_ship_sizes(game_file):
    """ (file open for reading) -> list of int

    Return the ship sizes that are found in game_file, a file that is open
    for reading. 
    """

    ship_sizes = game_file.readline().split()
    for i in range(len(ship_sizes)):
        ship_sizes[i] = int(ship_sizes[i])

    return ship_sizes

def get_symbol_board(game_file):
    """ (file open for reading) -> list of list of str

    Return the symbol board that is found in game_file, a file that is open
    for reading.
    """
    
    board = []
    
    for line in game_file:
        line = line.strip()
        sublist = []
        for char in line:
            sublist.append(char)
        board.append(sublist)

    return board

def get_valid_filename(msg):
    """ (str) -> str

    Prompt the user, using msg, to type the name of a file. This file should 
    exist in the same directory as the python file being executed. If a file 
    with the given name does not exist, keep re-prompting until the user gives
    a valid filename.  Return the name of that file.
    """
    
    filename = input(msg)
    while not os.path.exists(filename):
        print('That file does not exist.')
        filename = input(msg)

    return filename
    
def is_hit(row, col, symbol_board):
    """ (int, int, list of list of str) -> bool

    Return True if and only if symbol_board cell with row position row and 
    column position col is not EMPTY.

    >>> board = [[EMPTY,'b',EMPTY], [EMPTY,'b',EMPTY], [EMPTY,EMPTY,EMPTY]]
    >>> is_hit(0, 1, board)
    True
    >>> is_hit(2, 2, board)
    False
    """
    
    return symbol_board[row][col] != EMPTY

def is_not_unknown(row, col, view_board):
    """ (int, int, list of list of str) -> bool

    Return True if and only if view_board cell with row position row and 
    column position col is not UNKNOWN.

    >>> board = [['a',UNKNOWN], [UNKNOWN,'b']]
    >>> is_not_unknown(1, 1, board)
    True
    >>> is_not_unknown(0, 1, board)
    False
    """
    
    return view_board[row][col] != UNKNOWN

def place_ship(row1, col1, row2, col2, symbol_board, ship_symbol):
    """ (int, int, int, int, list of list of str, str) -> NoneType

    Precondition: len(ship_symbol) == 1

    Place the ship ship_symbol on the board from (row1, col1) to 
    (row2, col2), inclusive.

    >>> board = [[EMPTY,EMPTY,EMPTY], [EMPTY,EMPTY,EMPTY], [EMPTY,EMPTY,EMPTY]]
    >>> place_ship(0, 0, 1, 0, board, 'd')
    >>> board 
    [['d', '.', '.'], ['d', '.', '.'], ['.', '.', '.']]
    >>> place_ship(0, 1, 0, 2, board, 'z')
    >>> board 
    [['d', 'z', 'z'], ['d', '.', '.'], ['.', '.', '.']]
    """

    if row1 == row2:
        # place the ship horizontally
        for col in range(col1, col2 + 1):
            symbol_board[row1][col] = ship_symbol
    else:
        # place the ship vertically
        for row in range(row1, row2 + 1):
            symbol_board[row][col1] = ship_symbol
    
def print_sunk_message(ship_size, ship_label):
    """ (int, str) -> NoneType
  
    Print a message telling player that a ship_size ship with ship_label
    has been sunk.
    """

    print('The size {0} {1} ship has been sunk!'.format(ship_size,ship_label))
    
def update_after_hit(row, col, symbol_board, ships, sizes, hits_list):
    """ (int, int, list of list of str, list of str, list of int, list of int) 
          -> NoneType

    Modify symbol_board and hits_list to account for a hit of the cell 
    with row position row and column position col. Report a sunk ship.
    """
    
    ship_index = ships.index(symbol_board[row][col])
    hits_list[ship_index] = hits_list[ship_index] - 1
    if hits_list[ship_index] == 0: 
        print_sunk_message(sizes[ship_index],ships[ship_index])
    symbol_board[row][col] = symbol_board[row][col].upper()

def verify_game_parameters(board, ships, sizes):
    """ (list of list of str, list of str, list of int) -> bool

    Return True if and only if board is square with at least one cell and 
    at most MAX_BOARD_SIZE cells per row, the number of ship labels is the 
    same as the number of ship sizes, that there is at least one ship, all 
    ships have a valid size, and all ships have a valid, unique label.

    >>> board = [['.','b','.'], ['.','b','.'], ['a','a','a']]
    >>> ships = ['a', 'b']
    >>> sizes = [3, 2]
    >>> verify_game_parameters(board, ships, sizes)
    True
    >>> board = []
    >>> ships = ['a', 'd', 'h', 'i', 'n']
    >>> sizes = [1, 1, 1, 2, 1]
    >>> verify_game_parameters(board, ships, sizes)
    False
    """

    # Confirm that the board has a valid number of rows.
    if len(board) == 0 or len(board) > MAX_BOARD_SIZE:
        return False
    
    # Confirm that the board is square.
    for row in range(len(board)):
        if len(board[row]) != len(board):
            return False

    # Confirm that number of ships is the same as the number of ship sizes.
    if len(ships) != len(sizes):
        return False

    # Confirm that the ships and sizes lists are not empty.
    if len(ships) == 0:
        return False

    # Confirm that each ship has a valid size.
    for i in range(len(sizes)):
        if sizes[i] < MIN_SHIP_SIZE or sizes[i] > MAX_SHIP_SIZE:
            return False

    # Confirm that each ship has a valid unique label.
    for i in range(len(ships)):
        if len(ships[i]) > 1:
            return False
        else:
            for j in range(len(ships)):
                if i != j and ships[i] == ships[j]:
                    return False

    return True
    
def make_computer_symbol_board(board_size, ships, sizes):
    """ (int, list of str, list of int) -> list of list of str

    Return a new board_size by board_size symbol board with the ship symbols
    in ships and ship sizes in sizes placed randomly on the symbol board, either
    horizontally or vertically, and the rest of the cells EMPTY.
    """
    
    # make a board_size by board_size board that is entirely EMPTY
    board = []
    for row in range(board_size):
        board.append([])
        for column in range(board_size):
            board[row].append(EMPTY)   
    
    for index in range(len(ships) - 1, -1, -1):
        # get the ship symbol and its size
        placed = False
        ship = ships[index]
        ship_size = sizes[index]

        while not placed:
            
            # randomly generate a location at which to place the ship
            start_row = random.randint(0, board_size - 1)
            start_col = random.randint(0, board_size - 1)
            
            # randomly determine whether to place horizontally or vertically
            direction = random.randint(0, 1)
            
            if direction == 0:
                # calculate the (row, col) coordinates for horizontal placement
                end_row = start_row
                end_col = start_col + ship_size - 1
            else:
                # calculate the (row, col) coordinates for vertical placement
                end_row = start_row + ship_size - 1
                end_col = start_col
            
            # If the start and end locations are within the bounds of the board
            # and the cells are not occupied, place the ship.
            if (in_bounds(start_row, start_col, board_size) and 
                in_bounds(end_row, end_col, board_size)\
                and not is_occupied(start_row, start_col, end_row, end_col, 
                                    board)):
                place_ship(start_row, start_col, end_row, end_col, board, ship)
                placed = True
        
    return board
                
def main_single_player():
    """ () -> NoneType

    A single player game with no opponent.  This may be used for the purpose
    of testing our functions.
    """
    
    filename = get_valid_filename('Game filename: ')
    game_file = open(filename)
    ships = get_ship_labels(game_file)
    sizes = get_ship_sizes(game_file)
    symbol_board = get_symbol_board(game_file)
    if ( not verify_game_parameters(symbol_board, ships, sizes) or 
         not verify_symbol_board(symbol_board, ships, sizes)):
        print('The supplied game is not valid.  Game exiting.')
        return
    view_board = get_view_board(len(symbol_board))
    display_boards(view_board, symbol_board)
    hits_list = sizes[:]
    
    while not is_win(hits_list):
        
        print()
        print('Take a turn.')
        [row, col] = make_move(view_board)
        
        print()
        if is_hit(row, col, symbol_board):
            print('You hit a ship!')
            update_after_hit(row, col, symbol_board, ships, sizes, hits_list)
        else:
            print('You missed!')

        update_view_board(row, col, view_board, symbol_board)
        display_boards(view_board, symbol_board)
    
    print()
    print('You won in {0} move(s)!'.format(get_num_moves(view_board)))


def make_computer_move(view_board):
    """ (list of list of str) -> list of int
    
    Return the randomly generated row and column of the computer's next move.
    """
    
    board_size = len(view_board)

    row = random.randint(0, board_size - 1)    
    col = random.randint(0, board_size - 1)
    
    while is_not_unknown(row, col, view_board):
        row = random.randint(0, board_size - 1)    
        col = random.randint(0, board_size - 1)

    return [row, col]


def main_versus_computer():
    """ () -> NoneType

    Play the game with a single player vs. the computer.
    """
        
    filename = get_valid_filename('Game filename: ')
    game_file = open(filename)
    ships = get_ship_labels(game_file)
    sizes = get_ship_sizes(game_file)
    symbol_board_player = get_symbol_board(game_file)
    if ( not verify_game_parameters(symbol_board_player, ships, sizes) or
         not verify_symbol_board(symbol_board_player, ships, sizes)):
        print('The supplied game is not valid.  Game exiting.')
        return
    board_size = len(symbol_board_player)
    view_board_player = get_view_board(board_size)
    hits_player = sizes[:]
    
    symbol_board_computer = make_computer_symbol_board(board_size, ships, sizes)
    view_board_computer = get_view_board(board_size)
    hits_computer = sizes[:]
    
    player_turn = True

    while not is_win(hits_player) and not is_win(hits_computer):
        
        print()
        print()
        print()
        print(':' * 40)
        print()
        if player_turn:        
            symbol_board = symbol_board_computer
            view_board = view_board_player
            display_boards(view_board_player, symbol_board_player)
            print('Your turn.')
            [row, col] = make_move(view_board)
            hits_list = hits_player
        else:
            symbol_board = symbol_board_player
            view_board = view_board_computer
            display_boards(view_board_player, symbol_board_player)
            [row, col] = make_computer_move(view_board)
            hits_list = hits_computer
                    
        print()
        if is_hit(row, col, symbol_board):
            if player_turn:
                print('You hit a ship!')
            else:
                print('Computer hit a ship!')
            update_after_hit(row, col, symbol_board, ships, sizes, hits_list)
        else:
            if player_turn:
                print('You missed!')
            else:
                print('Computer missed!')
        print()
      
        update_view_board(row, col, view_board, symbol_board)
        display_boards(view_board_player, symbol_board_player)
        input('Press enter.\n')
        player_turn = not player_turn
        
    print()
    if is_win(hits_player):
        print('You won in {0} move(s)!'.format(
            get_num_moves(view_board_player)))
    else:
        print('The computer won in {0} move(s).  Please try again.'.format(
            get_num_moves(view_board_computer)))
    
    
if __name__ == '__main__':

    # uncomment these two lines to run the docstring examples
    #import doctest
    #doctest.testmod()
       
    # put a comment marker in front of one of these statements to deselect it
    #main_single_player()
    #main_versus_computer

    def is_win(list_hit):
        Result = True
        for int in list_hit:
            if int != 0:
                Result = False
            return Result
