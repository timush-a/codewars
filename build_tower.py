"""
Build Tower by the following given argument:
number of floors (integer and always greater than 0).
Tower block is represented as *
Python: return a list;
Have fun!
for example, a tower of 3 floors looks like below
[
  '  *  ', 
  ' *** ', 
  '*****'
]
and a tower of 6 floors looks like below
[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]
"""


def tower_builder(floors):
    tower = []
    star_per_lvl = 1
    max_length = 2 * floors - 1
    for a in range(1, floors + 1):
        tower.append(("*" * star_per_lvl).center(max_length))
        star_per_lvl += 2
    return tower
