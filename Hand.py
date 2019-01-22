# class Hand
# 是一个玩家的一手牌

from DefMahjong import SUITS, WAN, TIAO, TONG, Location

class Hand(object):
    def __init__(self, player_no):
        self.player_loc = Location(player_no)  # a bit strange. Location should apply to tiles.
        self.all_tiles = []
        self.tiles = []
        self.pongs = []  # stores tuples of triplets
        self.gongs = []  # stores tuples of quaruplets
        self.flag14tiles = False  # True for 14, False for 13

    def drawATile(self, tile):
        # need to ensure input is a tile?
        self.all_tiles.append(tile)
        tile['location'] = self.player_loc
    
    def sortHand(self):
        # self.all_tiles.sort(key = lambda t: t['suit'].value)
        # self.all_tiles.sort(key = lambda t: t['num'])
        # self.tiles.sort(key = lambda t: t['suit'].value)
        # self.tiles.sort(key = lambda t: t['num'])
        self.all_tiles.sort(key = lambda t: t.suit.value)
        self.all_tiles.sort(key = lambda t: t.num)
        self.tiles.sort(key = lambda t: t.suit.value)
        self.tiles.sort(key = lambda t: t.num)

    def discardATile(self, tile_to_discard):
        if not self.flag14tiles or len(self.all_tiles) <= 13:
            print('ERROR! In discardATile, not enough tiles to discard.')
            # raise exception!
            return None

        if tile_to_discard in self.tiles:
            self.tiles.remove(tile_to_discard)
            self.all_tiles.remove(tile_to_discard)
            self.flag14tiles = False
            return tile_to_discard
        else:
            print('ERROR! In discardATile, does not have this tile.')
            # raise exception!
        return None
