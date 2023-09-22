'''用所学的知识写一个斗地主随机发牌程序，将每个人的发牌以及多的三张牌的结果分别按照从大到小的顺序输出到player1.txt，player2.txt，player3.txt，others.txt四个文件中'''
'''Using H S C D to substitude hearts, spades, clubs, and diamonds'''
import random
import os
import re

def make_folder(name):
    '''to make a folder'''
    path = os.getcwd()
    folder = path + r'\\'+name
    if not os.path.exists(folder):
        os.makedirs(folder)
        print('---  Make a new folder successfully  ---')
    else:
        print("---  There is this folder!  ---")
    return folder

def substitude(card):
    ''' to substitude some nums to character'''
    num = re.findall('\d+',card)[0]
    if num == '1':
        ncard = card.replace(num,'A')
    elif num == '11':
        ncard = card.replace(num,'J')
    elif num == '12':
        ncard = card.replace(num,'Q')
    elif num == '13':
        ncard = card.replace(num,'K')
    elif num == '100':
        ncard = card.replace(num,'joker')
    elif num == '200':
        ncard = card.replace(num,'JOKER')
    else:
        ncard = card
    return ncard

cards=[]
for i in range(1,14):
    for suit in ["-H","-S","-C","-D"]:
        cards.append(str(i)+suit)
cards.append('100')#joker=100
cards.append('200')#JOKER=200
random.shuffle(cards)

player1,player2,player3=[],[],[]
players = [player1,player2,player3]
landowner = cards[-3:]

n=0
while n<= len(cards)-3:
    for player in players:
        player.append(cards[n])
        n+=1

player1.sort(reverse=True,key=lambda l: int(re.findall('\d+',l)[0]))
player2.sort(reverse=True,key=lambda l: int(re.findall('\d+',l)[0]))
player3.sort(reverse=True,key=lambda l: int(re.findall('\d+',l)[0]))
folder = make_folder('Q2_poke_game')

with open(folder + '\Player1.txt','w') as df:
    for card in player1:
        card = substitude(card)
        df.write(card+' ')

with open(folder + '\Player2.txt','w') as df:
    for card in player2:
        card = substitude(card)
        df.write(card+' ')

with open(folder + '\Player3.txt','w') as df:
    for card in player3:
        card = substitude(card)
        df.write(card+' ')

print('done')


