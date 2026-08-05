"""
    2. 题目二: 斗地主游戏【选做】
    需求描述 : 在三人斗地主游戏中一副扑克牌有54张牌 , 除了大王和小王之外剩余52张牌, 每张牌由点数和花色组成
    花色 : ♥️ ⬛️ ♠️ ♣️
    点数 : 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , J , Q , K , A
    基于斗地主游戏的背景完成如下需求 :
    1. 做牌 : 通过程序组合点数和花色生成54张牌(加上大王和小王)
    2. 洗牌 : 将54张扑克牌的顺序随机打乱
      1. 随机索引  --> 数据交换
      2. random.shuffle(列表)
    3. 发牌 : 提示用户录入三名玩家的姓名 , 录入完毕为每一个玩家发牌
      1. 玩家姓名 : [A,B,C]
      2. 发牌之后的结果 : {'A':[手牌],'B':[手牌],'C':[手牌],'底牌':[三张底牌]}
    4. 理牌 : 按照点数对玩家手牌进行排序
      1. 问AI参考
    5. 看牌 : 打印每个玩家的手牌以及底牌
      1. 循环遍历打印
"""
import random

# 四个花色
suits = ["♥", "♦", "♠", "♣"]
# 除去大小王的面值
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# 存放卡排的数组
cards = [("","大王"),("","小王")]

# 创建卡牌，最后添加大小王
for suit in suits:
    # 外层循环拿到每个花色，内层循环将所有的数字拼接到花色上
    for rank in ranks:
        cards.append((suit,rank))

# print(cards)

# 打乱原数组，进行交换
for current_card_index in range(len(cards)):
    # 随机创造一个索引
    # randint方法会包含end，会出现越界问题
    index = random.randint(0,len(cards) - 1)
    # 将当前索引的卡和随机索引对调
    cards[current_card_index],cards[index] = cards[index],cards[current_card_index]

# print(cards)

# 3. 发牌 : 提示用户录入三名玩家的姓名 , 录入完毕为每一个玩家发牌
#       1. 玩家姓名 : [A,B,C]
#       2. 发牌之后的结果 : {'A':[手牌],'B':[手牌],'C':[手牌],'底牌':[三张底牌]}

# 存储三个玩家
play_gamers = []
for _ in range(3):
    name = input('请输入玩家姓名：')
    play_gamers.append(name)

# 为每一位玩家发牌
# 发牌结果
play_start_result = {
    play_gamers[0]:[],
    play_gamers[1]:[],
    play_gamers[2]:[],
    "底牌":[]
}
# 循环发牌
for card_index in range(0,len(cards) - 3,3):
    # 每次发3张牌
    play_start_result[play_gamers[0]].append(cards[card_index])
    play_start_result[play_gamers[1]].append(cards[card_index + 1])
    play_start_result[play_gamers[2]].append(cards[card_index + 2])

# 循环发完牌之后，将最后三张牌放入底牌的数组
play_start_result["底牌"] = cards[-3:]

# print(play_start_result)

# 4. 理牌 : 按照点数对玩家手牌进行排序
# 权重
rank_weight = {
    "3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,
    "J":11,"Q":12,"K":13,"A":14,"2":15,"小王":20,"大王":21
}
# 将玩家手里的排进行排序
# 第一层循环遍历玩家
for gamer,card_list in play_start_result.items():
    # 将卡片排序好后，再塞回对应的玩家手里
    # 准备好每个玩家的排卡结果，赋值回玩家手中
    result_list = []

    # 第二层循环遍历每一张卡，拿到每张卡的权重
    for card_item in card_list:
        # print(card_item[-1])
        # 每个card_item是一个元组，取出2号元素，通过权重取出值进行比较大小，从头遍历到尾
        # 拿到当前需要插入的卡片的面值
        current_card = card_item[-1]
        # 匹配权重
        weight = rank_weight[current_card]
        inserted = False

        # 第三层循环，比较有序区的卡片，如果大则放结果数组最后
        # 将当前卡片跟有序区依次比较权重
        for i in range(len(result_list)):
            # 如果当前权重小于result有序区的卡片权重，则在该位置插入卡片，python中insert过后另一张卡片自动后移
            if weight < rank_weight[result_list[i][-1]]: # 排序好的卡片列表当中，i拿到元组 -1 拿到面值，去匹配权重
                # current_card是面值，第二层for循环本轮card_item才是卡片元组
                result_list.insert(i,card_item)
                # 插入完成，直接退出循环
                inserted = True
                break
        # 如果当前卡片result循环完了，没比较到东西，或者它本身就是最大的，if会失效
        # 直接插入到结果result的最后
        if not inserted:
            result_list.append(card_item)

    # 第二层循环后，本轮result_list排序完毕，将排序下一个游戏玩家
    play_start_result[gamer] = result_list

# 排序完成
print(play_start_result)

# 随机选中一位玩家作为地主，将底牌拼接给它
# --- 选地主逻辑 ---
landlord = random.choice(play_gamers)
print(f"\n🎉 恭喜玩家 【{landlord}】 成为地主，获得 3 张底牌！")
# 底牌拼接过去
play_start_result[landlord] += play_start_result['底牌']
del play_start_result['底牌']

# 最终循环输出结果
for player,card_list in play_start_result.items():
    print(f'玩家：{player}的手牌是：{card_list}')