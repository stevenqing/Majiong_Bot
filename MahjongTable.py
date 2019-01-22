# class MahjongTable
from random import shuffle
from enum import Enum

from DefMahjong import SUITS, WAN, TIAO, TONG
from Tile import TILES, FLATTEN_TILES, initMahjongTiles, setAllTilesLocToWall
from Hand import Hand

class MahjongTable(object):
    def __init__(self):
        initMahjongTiles()
        self.wall = [ i for i in range(108) ]  # 未抓取的牌堆, id 表示
        self.player_hands = [ Hand(i) for i in range(4) ]  # one hand represents one player
        self.discard_pile = [ [] for i in range(4) ]
        shuffle(self.wall)
        setAllTilesLocToWall()

    def init_game(self):
        for hand in self.player_hands:
            for i in range(13):
                hand.drawATile(FLATTEN_TILES[self.wall.pop(0)])
                

