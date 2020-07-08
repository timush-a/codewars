"""
DESCRIPTION
Task
Given two cells on the standard chess board, determine whether they have the same color or not.
Example
For cell1 = "A1" and cell2 = "C3", the output should be true.
For cell1 = "A1" and cell2 = "H3", the output should be false.
true if both cells have the same color, false otherwise.
"""


def chess_board_cell_color(cell1, cell2):
    columns = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    same_colors = False
    if ((columns[cell1[0]] + int(cell1[1])) % 2 == 0 and (columns[cell2[0]] + int(cell2[1])) % 2 == 0):
        same_colors = True
    elif ((columns[cell1[0]] + int(cell1[1])) % 2 == 1 and (columns[cell2[0]] + int(cell2[1])) % 2 == 1):
        same_colors = True
    return same_colors
