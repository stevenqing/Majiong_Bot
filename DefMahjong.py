# definition of all tiles, 3 suits
# class Tile, enum SUITS

from enum import Enum

# enum Location
# identifies location of a tile
class Location(Enum):
    player0 = 0
    player1 = 1
    player2 = 2
    player3 = 3
    wall = 4
    discard_pile = 5

class SUITS(Enum):
    WAN = 0
    TIAO = 1
    TONG = 2

WAN = SUITS.WAN
TIAO = SUITS.TIAO
TONG = SUITS.TONG
