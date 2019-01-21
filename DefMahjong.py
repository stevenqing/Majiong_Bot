# definition of all tiles, 3 suits
# class Tile, enum SUITS

from enum import Enum

class SUITS(Enum):
    WAN = 0
    TIAO = 1
    TONG = 2

TILES = [] # a flatten list of all tiles
WAN_TILES =  [ [] for i in range(9) ] #WAN1, WAN2, WAN3, WAN4, WAN5, WAN6, WAN7, WAN8, WAN9]
TIAO_TILES = [ [] for i in range(9) ] #TIAO1, TIAO2, TIAO3, TIAO4, TIAO5, TIAO6, TIAO7, TIAO8, TIAO9]
TONG_TILES = [ [] for i in range(9) ] #TONG1, TONG2, TONG3, TONG4, TONG5, TONG6, TONG7, TONG8, TONG9]

# data structure of a tile
<TYPE>_TILES[M][K]= {
    'id': SUITS.<TYPE>.value * 36 + M*4 + K, # how id correspond to tile objects
    'suit': SUITS.<TYPE>,
    'num': M+1,
    'location': None  # Stores where this tile is located
}

3 * 9 * 4 == 108

def initMahjongTiles():

    id = 0
    for i in range(9):
        for j in range(4):
            WAN_TILES[i].append({
                'id': id,
                'suit': SUITS.WAN,
                'num': i+1,
                'location': None
            })
            TILES.append(WAN_TILES[-1])
            id += 1

    for i in range(9):
        for j in range(4):
            TIAO_TILES[i].append({
                'id': id,
                'suit': SUITS.TIAO,
                'num': i+1,
                'location': None
            })
            TILES.append(TIAO_TILES[-1])
            id += 1

    for i in range(9):
        for j in range(4):
            TONG_TILES[i].append({
                'id': id,
                'suit': SUITS.TONG,
                'num': i+1,
                'location': None
            })
            TILES.append(TONG_TILES[-1])
            id += 1


