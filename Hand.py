# class Hand

import DefMahjong
from DefMahjong import TILES, WAN_TILES, TIAO_TILES, TONG_TILES, SUITS
# from MahjongTable import Location

class Hand(object):
    def __init__(self, player_no):
        self.player_loc = Location(player_no)  # a bit strange. Location should apply to tiles.
        self.all_tiles = []
        self.tiles = []
        self.pongs = [] # stores only one item of the triplet
        self.gongs = [] # stores only one item of the quaruplet
        self.flag14tiles = False

    def drawATile(self, tile):
        self.all_tiles.append(tile)
        tile['location'] = self.player_loc
    
