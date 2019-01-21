# class MahjongTable
from random import shuffle
from enum import Enum

import DefMahjong
from DefMahjong import TILES, WAN_TILES, TIAO_TILES, TONG_TILES, SUITS
from Hand import Hand

# Enumeration Location
# identifies location of a tile
class Location(Enum):
    player0 = 0
    player1 = 1
    player2 = 2
    player3 = 3
    wall = 4
    discard_pile = 5

class MahjongTable(object):

    def __init__(self):
        DefMahjong.initMahjongTiles()
        self.player_hands = [ Hand(i) for i in range(4) ]  # one hand represents one player
        self.discard_pile = []
        self.wall = [ i for i in range(108) ]  # 未抓取的牌堆, id 表示
        # t['location'] = Location.wall for t in TILES
        shuffle(self.wall)

    def init_game(self):
        for i, hand in enumerate(self.player_hands):
            for i in range(13):
                hand.drawATile(self.wall.pop(0))
                

