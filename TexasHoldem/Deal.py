from TexasHoldem.entity.Poke import Poke
import random


# 初始化52张牌
def initpoke():
    color = ['♠', '♥', '♣', '♦']
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    poke_list = []
    for i in color:
        for j in numbers:
            poke = Poke(i, j)
            poke_list.append(poke)
    return poke_list


# 洗牌
def shuffle(poke_list):
    random.shuffle(poke_list)
    return poke_list


# 发手牌  players  玩家数量
def deal(players, poke_list):
    hand_list = []
    for i in range(players):
        player_hand = [poke_list[i], poke_list[i + players]]
        hand_list.append(player_hand)
    for i in range(players * 2):
        poke_list.remove(poke_list[0])
    return hand_list


# 翻牌
def flop(poke_list):
    poke_list.remove(poke_list[0])
    flop_list = []
    for i in range(3):
        flop_list.append(poke_list[i])
    for j in range(3):
        poke_list.remove(poke_list[0])
    return flop_list


# 转牌和河牌
def turn_and_river(poke_list):
    poke_list.remove(poke_list[0])
    turn = poke_list[0]
    return turn


if __name__ == '__main__':
    poke_list = initpoke()
    # poke_list = shuffle(poke_list)
    nums = input("发牌，输入玩家人数：")
    hands = deal(int(nums), poke_list)
    count = 1
    for hand in hands:
        print("玩家" + str(count) + "手牌")
        hand[0].printpoke()
        hand[1].printpoke()
        count += 1

    if_flop = input("是否进入翻牌圈，请输入1翻牌：")
    flop_list = flop(poke_list)
    if if_flop == '1':
        for flop in flop_list:
            flop.printpoke()

    if_turn = input("是否发进入转牌圈，请输入1转牌：")
    turn = turn_and_river(poke_list)
    if if_turn == '1':
        turn.printpoke()

    if_river = input("是否进入河牌圈，请输入1河牌：")
    river = turn_and_river(poke_list)
    if if_river == '1':
        river.printpoke()
