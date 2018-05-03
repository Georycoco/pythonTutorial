#person1 = input('Are you coming?');
#person2 = input('Are you coming?');

#if person1 == '来' or person2 == '来':   # python使用 "or"和"and" 表示 "||"和"&&"
#    print('pointment booked!'); 

'''
if person1 == '来' and person2 == '来':
    print('pointment booked!'); 
'''

sex = input('你的性别: ');
deposit = input('你的存款： ');
monthly_Income = input('你的月收入: ');
house = input('你的固定资产价值: ');
color = input('你白吗？');
beauty = input('你美吗？');
deposit_Num = int(deposit);
monthly_Income_Num = int(monthly_Income);
house_Value = int(house); 

total_Asset = deposit_Num + monthly_Income_Num + house_Value;


if total_Asset >= 500000 and total_Asset <=1000000 and sex =='男':
    print('YOu are fine');

if sex == '女' and color == '白' or beauty == '美' and total_Asset >= 1000000:
    print('白～富～美～!');
    print('好羡慕～～～!');
else: 
    print('Fuck the world if You Are Rich, otherwise, Fuck~Your~Self!');