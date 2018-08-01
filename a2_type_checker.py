import builtins

# Check for use of functions print and input.

our_print = print

def disable_print(*args):
    raise Exception("You must not call print anywhere except make_move!")

def disable_input(*args):
    raise Exception("You must not call input anywhere except make_move!")

builtins.print = disable_print
builtins.input = disable_input



import battleship

def is_board(lst):
    """ (object) -> bool
    
    Return True iff lst is a list of list of str.
    
    >>> is_board([['a', 'b', 'c']])
    True
    """
    
    if not isinstance(lst, list):
        return False
        
    for element in lst:
        if not isinstance(element, list):
            return False
        for s in element:
            if not isinstance(s, str):
                return False
    return True
    

# Get the initial value of the constants
constants_before = [1, 10, '-', '.', 'X', 'M']

# Type check battleship.is_win
result = battleship.is_win([1, 2, 3])
assert isinstance(result, bool), \
       '''battleship.is_win should return a bool, but returned {0}
       .'''.format(type(result))

# Type check battleship.get_view_board
result = battleship.get_view_board(5)
assert is_board(result), \
       '''battleship.get_view_board should return a list of list of str!'''

# Type check battleship.is_occupied
symbol_board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
result = battleship.is_occupied(0, 0, 1, 1, symbol_board)
assert isinstance(result, bool), \
       '''battleship.is_occupied should return a bool, but returned {0}
       .'''.format(type(result))

# Type check battleship.update_view_board
view_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
symbol_board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
result = battleship.update_view_board(0, 0, view_board, symbol_board)
assert result is None, \
       '''battleship.update_view_board should return None, but returned {0}
       .'''.format(type(result))

# Type check battleship.get_num_moves
view_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
result = battleship.get_num_moves(view_board)
assert isinstance(result, int), \
       '''battleship.get_num_moves should return an int, but returned {0}
       .'''.format(type(result))

# Type check battleship.verify_symbol_board
symbol_board = [['a', 'a', 'a'], ['b', 'b', '.'], ['.', '.', '.']]
ships = ['a', 'b']
sizes = [3, 2]
result = battleship.verify_symbol_board(symbol_board, ships, sizes)
assert isinstance(result, bool), \
       '''battleship.verify_symbol_board should return a bool, but returned {0}
       .'''.format(type(result))


# Get the final values of the constants
constants_after = [battleship.MIN_SHIP_SIZE, battleship.MAX_SHIP_SIZE, battleship.UNKNOWN, battleship.EMPTY, battleship.HIT, battleship.MISS]


# Check whether the constants are unchanged.
assert constants_before == constants_after, \
       '''Your function(s) modified the value of one or more constants.
       Edit your code so that the value of the constants are not 
       changed by your functions.'''
    
    

our_print("""

The type checker passed.

This means that your functions in battleship.py:
- are named correctly,
- take the correct number of arguments, and
- return the correct types.  

This does NOT mean that the functions are correct!

Be sure to thoroughly test your functions yourself before submitting.""")

