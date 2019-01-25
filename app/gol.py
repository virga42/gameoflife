"""
Conway's Game of Life

Implemented by Tom Callahan
1/20/19
"""
import functools

def string_to_universe(s, width):
    """
    String, Int -> Array
    Takes a string of char and width of row and returns an array of rows
    If string is not divisible by width extra characters are dropped
    """   
    if s == '':
        return []
    elif width == 0:
        return []
    elif len(s) % width != 0:
        remainder = len(s) % width
        return string_to_universe(s[:-remainder], width)
    else:
        # convert string of characters to list of ints
        ints = [int(c) for c in s]
        # return list of rows with width number of ints
        return [ints[i:i+width] for i in range(0, len(ints), width)]

def neighbor_addresses(row, col):
    """ 
    Int Int -> Array
    Returns a list of neighbor addresses for a row and column
    Note: generated addresses may be off the board 
    """
    return [[row-1, col-1], [row-1, col], [row-1, col+1], \
            [row, col-1], [row, col+1], \
            [row+1, col-1], [row+1, col], [row+1, col+1]]

def address_valid(row, col, width, height):
    """
    Int Int Int Int -> Boolean
    Returns true if a given row and col is on a board with given width and height
    """
    if row >= 0 and row < height and col >= 0 and col < width:
        return True
    else:
        return False

def neighbor_population(universe, width, row, col):
    """
    Array Int Int Int -> Int
    Returns the number of neighbors around a cell at row and col position
    """
    height = len(universe)
    
    # calculate candidate neighbor addresses
    neighbor_candidates = neighbor_addresses(row, col)

    # filter for valid addresses only
    valid_neighbors_addresses = [[row, col] for row, col in neighbor_candidates \
                                    if address_valid(row, col, width, height)]

    neighbor_values = [universe[row][col] for row, col in valid_neighbors_addresses]
    
    return sum(neighbor_values)

def cell_reckoning(universe, width, row, col):
    """ 
    Array Int Int Int -> 0 or 1
    Returns the fate of a given cell based on the number of its neighbors
    0 for death and 1 for birth/survival
    """
    n = neighbor_population(universe, width, row, col)

    if universe[row][col] == 1:
        """ cell is already populated """
        if n == 0 or n == 1:
            return 0
        elif n == 2 or n == 3:
            return 1
        else:
            return 0
    else:
        """ cell is empty """
        if n == 3:
            return 1
        else: 
            return 0

def universe_generation(universe, width):
    """ 
    Array Int -> Array
    Returns the universe with cells' next generation
    """
    result = ""
    for r in range(len(universe)):
        for c in range(len(universe[r])):
            result += str(cell_reckoning(universe, width, r, c))
    return string_to_universe(result, width)


def universe_to_string(universe):
    """ 
    Array -> String
    Returns the string representation of a universe
    """
    s = ''
    for row in universe:
        s += ''.join(str(n) for n in row)
    return s

def figure_creator(fig, width, height):
    """
    Array Int Int -> String
    Returns the string of a universe with a given figure in its center
    """
    fig_h = len(fig)
    fig_w = len(fig[0])
    pad_top = int(((height - fig_h)) / 2)
    pad_bot = height - pad_top - fig_h 
    pad_lft = int(((width - fig_w) / 2))
    pad_rgt = width - pad_lft - fig_w

    str_top = pad_top * width * '0'

    str_middle = ''
    for r in fig:
        str_r = ''.join(str(e) for e in r)
        str_middle += (pad_lft * '0') + str_r + (pad_rgt * '0')

    str_bot = pad_bot * width * '0'

    return str_top + str_middle + str_bot    

glider = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
small_exploder = [[0, 1, 0], [1, 1, 1], [1, 0, 1], [0, 1, 0]]
exploder = [[1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1]]
ten_cell_row = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
lightweight_spaceship = [[0, 1, 1, 1, 1], [1, 0, 0, 0, 1], [0, 0, 0, 0, 1], [1, 0, 0, 1, 0]]
tumbler = [[0, 1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 1, 0], [0, 0, 1, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 1, 0, 0, 0, 1, 1]] 

