# 字典  index
# 如果相同信息用列表，类似 Array，信息不相同就用字典，类似 ArrayList
# p = list.index(value)  p 就是 value 在 list 中的 下标

student = ['CEO','VIC', 33]
print('%s  %d   %s'%(student[0],student[2],student[1]))


# informationi{key : value}
information = {'Name':'George', 'Address':'Melbourne', 'Age':27}  #用 ： 分割
print('%s  %d  %s'%(information['Name'],information['Age'],information['Address']))
print(information)

#添加
infor = {'Name':'George'}
infor['Age'] = 20
infor['QQ'] = 191081789
print(infor)

#修改
infor['Age'] = 23  #字典里会把key相同的元素值直接覆盖

#删除
del infor['QQ']

#查找 用 get(key) 查找如果没有就不返回，不会报错，如果infor['Money'] 会报错，程序停止
infor.get('QQ')
infor.get('Money')   


#判断 重点！！！！ 查找字典中的单个元素
infor = [{'Name':'George', 'Address':'Melbourne', 'Age':27},{'Name':'John', 'Address':'Melbourne', 'Age':28}]
print(infor)

for temp in infor:
    print(temp)

for temp in infor:
    print(temp['Name'])