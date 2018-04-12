#剪刀石头布
import random;


print('1 for paper')
print('2 for scissor')
print('3 for rock')
player = int(input('please select from above:'))
#player_Index = int(player);

computer = random.randint(1,3);

if (player == 3 and computer == 2) or (player == 2 and computer == 1) or (player == 1 and computer == 3):
    print('玩家获胜')
elif (computer == 3 and player == 2) or (computer == 2 and player == 1) or (computer == 1 and player == 3):
    print('电脑获胜')
elif computer == player:
    print('平局')
else:
    print('error');