#9*9 乘法表格

max = input('please enter a number less than 9: ');
i = 1;

max_Num = int(max);

while i <=max_Num:
    j=1;
    while j <= i:
        print('%d*%d=%d\t'%(j,i,i*j),end='');
        j+=1;
    print('');
    i+=1;  
print('end~~');