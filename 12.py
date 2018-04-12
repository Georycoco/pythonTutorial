#字符串组合

a = 'Lao';
b = 'Wang';
c = 'Zhao';

d = a + b;
print(d);

e = '===' + c + '===';
print(e);

f = '====%s===='%(a+c);
print(f);

#下标   类似Array
name = 'George';
print(name[0]); #'G'
print(name[2]); #'o'
print(name[-1]); #'e' 从后往前取

name = 'george','John','Mark';
print(name[1]); #'John'

#切片
letter = 'abcdefghijklmnopqrstuvwxyz';
print(letter[2:7]); #从下标2开始取到下标7前一个
print(letter[2:-2]); #从下表2开始取到倒数第三个
print(letter[2:]); #从下标2开始取到最后一个
print(letter[2:-1:2]); #从下表2开始取到倒数第三个，并且每2个数字取一个/每隔一个取 叫做补偿
print(letter[-1:1:-1]); #逆序 但只能取到第2个
print(letter[-1::-1]); # print(letter[::-1]); 因为第三个补偿是负数，所以会从右到左读取 
