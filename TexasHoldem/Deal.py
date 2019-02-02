from TexasHoldem.entity.Poke import Poke
import random


# 初始化52张牌
def initpoke():
    color = ['Spade', 'Hearts', 'Diamond', 'Club']
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
    return flop_list


# 转牌和河牌
def turn_and_river():
    poke_list.remove(poke_list[0])
    turn = poke_list[0]
    return turn


if __name__ == '__main__':
    poke_list = initpoke()
    poke_list = shuffle(poke_list)
    nums = input("发牌，输入玩家人数：")
    hands = deal(nums, poke_list)
    for hand in hands:
        count = 1
        print("玩家" + str(count) + "手牌")
        hand[0].printpoke()
        hand[1].printpoke()
        count += 1

    pass
