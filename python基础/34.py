# 给程序传参数

import sys

print(sys.argv)

# name = sys.argv[1]

# print('Welcome %s !!!'%name) #可以在程序外直接传入name的值


# 列表生成式
a = [i for i in range(1, 8)]
print(a)

b = [6 for i in range(1, 8)]
print(b)

c = [i for i in range(10) if i % 2 == 0]
print(c)

d = [i for i in range(3) for j in range(2)]
print(d)

e = [(i, j) for i in range(3) for j in range(2)]
print(e)

f = [(i, j, k) for i in range(3) for j in range(2) for k in range(2)]
print(f)


aa = (11,22,33,44,55,11,22,33)
bb = [11,22,33,11,22,33]
print(aa)
print(bb)
print(type(aa))
cc = set(bb) #set 也有去重效果
print(cc)
dd = list(cc)
print(dd)