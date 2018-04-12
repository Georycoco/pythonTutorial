#while 循环   
'''
a = 0;

while a <= 10:
    print(a);
    a = a+1;

print('end~');

i = 1

while i <=20:
     i = i+1;
     print(i);
print('end~');

#if嵌套
#max = input('please enter a nubmer:');
#max_Num = int(max);

ticket = input('enter 1 or 0:');
knifeLength = input('knife length:');
ticket_Index = int(ticket);
knifeLength_Index = int(knifeLength);

if ticket_Index == 1:
    print('you have a ticket');
    if knifeLength_Index <= 8:
        print('Welcome abord~Enjoy your trip');
    else:
        print('you can not abord with dangerous')
elif ticket == 0:
    print('you do not have a valid ticket');
    print('please buy from any counter');
else:
    print('get away~');
'''


sex = input('你的性别: ');

if sex == '男':
    print('survy for male:')
    deposit = input('你的存款： ');
    monthly_Income = input('你的月收入: ');
    house = input('你的固定资产价值: ');
    deposit_Num = int(deposit);
    monthly_Income_Num = int(monthly_Income);
    house_Value = int(house); 
    total_Asset = deposit_Num + monthly_Income_Num + house_Value;

    if total_Asset >= 1000000:
        print('Oh nice man!')
    else:
        print('pass');

elif sex == '女':
    print('survy for female')
    house = input('你的固定资产价值: ');
    color = input('你白吗？');
    beauty = input('你美吗？');
    house_Value = int(house);
    if color == '白' and beauty == '美' and house_Value >= 1000000:
        print('Wow, 白富美～～～');
    elif color == '白' or beauty == '美' and house_Value >= 500000 and house_Value <1000000:
        print('Oh, nice girl')
    else:
        print('Poor girl~~')
else:
    print('hard to say~~~~');