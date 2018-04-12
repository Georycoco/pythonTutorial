#打印图形

aa = 1;
while aa<=5:
    k = 1;
    while k <= 5:
        print('*', end='');    # end=''表示不换行打印
        k += 1;
    print('');  # 换行
    aa += 1;


#选择打多少行多少列
row = input('please enter row number:')
coloum = input('please enter coloum number:')
row_Num = int(row);
coloum_Num = int(coloum);

a=1;
b=1;
while a <=row_Num:
    
    while b<=row_Num:
        print('*'*coloum_Num);
        b += 1;
    a += 1;
print('end~~~~');



#三角形
i = 1;
j = 1;
while i <= 5:
    while j <= i:
        print('*'*j);
        j += 1;
    i += 1;
print('end~~');



a = 1;
c = 10;
while a <= 10:
    while c<=10:
        print(' '*c);
        c+=1;
    b=1;
    while b <=a:
        print('*', end='');
        b+=1;
    print('');
    a+=1;
print('end~~');

