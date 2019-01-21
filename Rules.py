# class Rule:
#
# deals with
# hand tiles validity; 
# Mahjong calling validity; 胡牌
#    缺一门

# import DefMahjong
from DefMahjong import TILES, WAN_TILES, TIAO_TILES, TONG_TILES, SUITS

class Rules(object):
    pass

hand = {
    'all_tiles': [],
    'tiles': [],
    'pongs': [], # stores tuple of triplet
    'gongs': [], # stores tuples of quaruplet
    'flag14tiles': False  # True for 14, False for 13
}

def sortHand(hand):
    hand.all_tiles.sort(key = lambda t: t.suit.value)
    hand.all_tiles.sort(key = lambda t: t.num)
    hand.tiles.sort(key = lambda t: t.suit.value)
    hand.tiles.sort(key = lambda t: t.num)



def isValidHand(hand):
    # check data validity
    if not (set(hand['tiles']).issubset(set(hand['all_tiles']))
        and set(hand['pongs']).issubset(set(hand['all_tiles'])) 
        and set(hand['gongs']).issubset(set(hand['all_tiles'])) ):
        return False
    # check number of tiles
    if len(hand.all_tiles) - len(hand.gongs) != 13:
        return False

    return True


def isSpecialWinnnigHand(hand):
    # 13yao, dasanyuan...
    pass
    return False

def isValidMahjongCall(hand):
    sortHand(hand)

    if not isValidHand(hand):
        return False

    if isSpecialWinnnigHand(hand):
        return True

    wans = getWans(hand['tiles'])  # use reduse()?
    tiaos = getTiaos(hand['tiles'])
    tongs = getTongs(hand['tiles'])

