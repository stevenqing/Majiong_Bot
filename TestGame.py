# this script is for module testing

from MahjongTable import MahjongTable

# START MAIN
mj_table = MahjongTable()
mj_table.init_game()

print(mj_table.player_hands[0].all_tiles)
mj_table.player_hands[0].sortHand()

print('After sortHand:')
print(mj_table.player_hands[0].all_tiles)

