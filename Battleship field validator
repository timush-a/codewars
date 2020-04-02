"""
Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.
Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.
Before the game begins, players set up the board and place the ships accordingly to the following rules:
There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
Each ship must be a straight line, except for submarines, which are just single cell.
The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.
This is all you need to solve this kata.
"""


def validate_battlefield(field):
    valid = True
    ones = 0
    for row in range(len(field)):
        for column in range(len(field)):
            if field[row][column]:
                ones += 1
    if ones != 20:
        valid = False
        
    for row in range(1, len(field) - 1):
        for column in range(1, len(field) - 1):
            if field[row][column] == 1 == field[row+1][column+1]:
                valid = False
            elif field[row][column] == 1 == field[row-1][column-1]:
                valid = False
            elif field[row][column] == 1 == field[row+1][column-1]:
                valid = False
            elif field[row][column] == 1 == field[row-1][column+1]:
                valid = False
    
    
    
    
    def count_battleships(field):
        nonlocal valid
        battleships = 0
        cruisers = 0
        destroyers = 0
        
        for row in zip(*field):
            string = ""
            for elem in row:
                string += str(elem)
            for ship in string.split('0'):
                if len(ship) == 4:
                    battleships += 1
                elif len(ship) == 3:
                    cruisers += 1
                elif len(ship) == 2:
                    destroyers += 1
                elif len(ship) > 4:
                    valid = False
                    return valid
                    
        for row in field:
            string = ""
            for elem in row:
                string += str(elem)
            for ship in string.split('0'):
                if len(ship) == 4:
                    battleships += 1
                elif len(ship) == 3:
                    cruisers += 1
                elif len(ship) == 2:
                    destroyers += 1
                elif len(ship) > 4:
                    valid = False
                    return valid
        
        if battleships != 1 or cruisers != 2 or destroyers != 3:
            valid = False
            return valid
            
    count_battleships(field)
    
    
    
    
    return valid
