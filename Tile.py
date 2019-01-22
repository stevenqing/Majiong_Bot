# class Tile

from DefMahjong import SUITS, WAN, TIAO, TONG, Location

WAN_TILES =  [ [] for i in range(9) ] #WAN1, WAN2, WAN3, WAN4, WAN5, WAN6, WAN7, WAN8, WAN9]
TIAO_TILES = [ [] for i in range(9) ] #TIAO1, TIAO2, TIAO3, TIAO4, TIAO5, TIAO6, TIAO7, TIAO8, TIAO9]
TONG_TILES = [ [] for i in range(9) ] #TONG1, TONG2, TONG3, TONG4, TONG5, TONG6, TONG7, TONG8, TONG9]
TILES = {
    WAN: WAN_TILES,
    TIAO: TIAO_TILES,
    TONG: TONG_TILES
}
# e.g. TILES[TIAO][1][2] gets you ErTiao2
FLATTEN_TILES = [] # a flatten list of all tiles
# e.g. FLATTEN_TILES[42] also gets you ErTiao2
# So, FLATTEN_TILES[42] is TILES[TIAO][1][2] --- is True!


# data structure of a tile. OBSOLETE! Use class Tile instead.
# <TYPE>_TILES[M][K]= {
#     'id': SUITS.<TYPE>.value * 36 + M*4 + K, # how id correspond to tile objects
#     'suit': SUITS.<TYPE>,
#     'num': M+1,
#     'location': None  # Stores where this tile is located
# }


class Tile(object):
    def __init__(self, uid):
        self.id = uid
        self.suit = SUITS(uid // 36)
        self.num = uid % 36 // 4 + 1
        self.location = None

    def __str__(self):
        return str(
            {1:'一', 2:'二', 3:'三', 4:'四', 5:'五', 6:'六', 7:'七', 8:'八', 9:'九'}[self.num] \
            + {WAN: '萬', TIAO: '条', TONG: '筒'}[self.suit] \
            # + '(' \
            + str(self.id - self.suit.value * 36 - (self.num-1)*4) \
            # + ')'
        )


def initMahjongTiles():
    uid = 0
    # 3 * 9 * 4 == 108
    for suit_i in SUITS:
        for num in range(9):
            for j in range(4):
                TILES[suit_i][num].append(Tile(uid))
                # {'id': id,
                #  'suit': SUITS(suit_no),
                #  'num': num+1,
                #  'location': None }
                FLATTEN_TILES.append(TILES[suit_i][num][-1])
                uid += 1

def setAllTilesLocToWall():
    for t in FLATTEN_TILES:
        t.location = Location.wall


t42 = Tile(42)
print(t42)

t42.id
t42.suit
t42.num
t42.location
