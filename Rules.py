# class Rule

# deals with
# hand tiles validity; 
# Mahjong calling validity; 胡牌
#    缺一门

from DefMahjong import SUITS, WAN, TIAO, TONG
from Hand import Hand  # for testing

class Rules(object):
    pass

def isValidHand(hand):

    hand = Hand(0)  # for testing
    # check data validity
    # if not (set(hand.tiles).issubset(set(hand.all_tiles))
    #     and set(hand.pongs).issubset(set(hand.all_tiles)) 
    #     and set(hand.gongs).issubset(set(hand.all_tiles)) ):
    #     return False
    if not set(hand.all_tiles) == set(hand.tiles +
            [t for triplet in hand.pongs for t in triplet] +
            [t for quadruplet in hand.gongs for t in quadruplet] ):
        return False

    # check number of tiles
    if not hand.flag14tiles:
        if len(hand.all_tiles) - len(hand.gongs) != 13: return False
    else:
        if len(hand.all_tiles) - len(hand.gongs) != 14: return False

    return True

def isSpecialWinnnigHand(hand):
    if not isValidHand(hand):
        return False
    # 13yao, dasanyuan...
    return False

def queYiMen(hand):
    return len(set([ t.suit for t in hand.all_tiles ])) <= 2

def getSuitFromList(target_suit, tiles):
    return [ t for t in tiles if t.suit is target_suit ]
    # return filter(lambda t: t.suit is target_suit, tiles)

def isValidMahjongCall(hand):
    hand.sortHand()

    if not isValidHand(hand):
        return False

    if isSpecialWinnnigHand(hand):
        return True

    # 接下来判断平胡
    if not queYiMen(hand):
        return False

    wans = getSuitFromList(WAN, hand.tiles)
    tiaos = getSuitFromList(TIAO, hand.tiles)
    tongs = getSuitFromList(TONG, hand.tiles)

    if len(wans)  in (1, 4, 7, 10) or\
    len(tiaos) in (1, 4, 7, 10) or\
    len(tongs) in (1, 4, 7, 10):
        return False
    

