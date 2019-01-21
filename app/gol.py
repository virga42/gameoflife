"""
Conway's Game of Life

Implemented by Tom Callahan
1/20/19
"""

def string_to_universe(s, width):
    """
    String, Int -> Array
    Takes a string of char and width of row and returns an array of rows
    If string is not divisible by width extra characters are dropped
    """   
    if s == "":
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
    Returns true is a given row and col is on a board with given width and height
    """
    if row < 0 or row > width-1:
        return False
    elif col < 0 or col > height-1:
        return False
    else:
        return True

def neighbor_population(universe, width, row, col):
    """
    Array Int Int Int -> Int
    Returns the number of neighbors around a cell at row and col position
    """
    height = len(universe)
    
    # calculate candidate neighbor addresses
    neighbor_candidates = neighbor_addresses(row, col)
    
    # filter for valid addresses only
    valid_neighbors_addy = [neighbor for neighbor in neighbor_candidates if address_valid(neighbor[0], neighbor[1], width, height)]

    # sum the number of neighbors
    total = 0
    for address in valid_neighbors_addy:
        total+= universe[address[0]][address[1]]

    return total

def generation(universe, width, row, col):
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

