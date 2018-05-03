# for 循环


name = 'laowang'

for temp in name:
    print('---')
    print(temp)



# print even number between 0 to 100
i = 0;
j = 0;
while i <= 100:
    if i%2 == 0:
        print(i);
        j+=1;
    if j == 20:
        break;
    i += 1;

# break 会终止整个循环并跳出

i = 0;
j = 0;
while i <= 100:
    if i%2 == 0:
        print(i);
        j+=1;
    if j == 20:
        continue;
    i += 1;

#continue 会在 i = 20 时跳出本次循环，不执行本次循环剩下的代码 然后重新开始新循环

i = 1;
j = 1;
while i <= 5:
    while j <= i:
        print('*'*j);
        j += 1;
        # break  此处的break只对里面的while循环起作用
    i += 1;
print('end~~'); 