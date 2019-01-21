cards=[]
WAN=[WAN1,WAN2,WAN3,WAN4,WAN5,WAN6,WAN7,WAN8,WAN9]
SUO=[SUO1,SUO2,SUO3,SUO4,SUO5,SUO6,SUO7,SUO8,SUO9]
TONG=[TONG1,TONG2,TONG3,TONG4,TONG5,TONG6,TONG7,TONG8,TONG9]
	
def Determine_The_Least(cards):#输入牌型，返回最少的花色
	discard_flower=[]
	for card in cards:
		if card is in WAN:
			count_wan+=1
		if card is in SUO:
			count_suo+=1
		if card is in TONG:
			count_tong+=1
	if count_wan>=count_suo:
		if count_suo>=count_tong:
			discard_flower=TONG
		else:
			discard_flower=SUO
	else:
		if count_wan>=count_tong:
			discard_flower=TONG
		else:
			discard_flower=WAN
return discard_flower

def Card_Shuffle(cards):
	for card in cards:
		if card is in WAN:
			count_wan+=1
		if card is in SUO:
			count_suo+=1
		if card is in TONG:
			count_tong+=1
	for card in cards:



def Main_Procedure(cards):
	discard_flower=Determine_The_Least(cards)
	
	for card in cards:
		if card is in discard_flower
			card_play=card



