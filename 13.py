#列表  相当于Array

name_List = ['George','John','Lina','Alex','Mars','Duke'];
print(name_List);

# 在列表中加入元素 
#  append  只会把值添加到最后面,并且一次只能添加一个
name_List.append('Tim');
print(name_List);

# insert  (0, 'Coco'), 在下标0的位置插入 'Coco'
name_List.insert(0,'Coco');
print(name_List);

# extend 
name_List_2 = ['王菲','梁朝伟','谢霆锋','张学友']
name = name_List + name_List_2; # 新建一个里表，相加原有列表
print(name);
name_List.extend(name_List_2); # 将第二个列表添加到地一个列表
print(name_List);


#删除元素
name_List.pop(); # pop() 每次删除最后一个元素
print(name_List);

name.remove('George'); # remove() 删除括号内的元素，如果有先同，删除第一个
print(name); 

del name[0]; # 删除对应下标的元素
print(name);


#修改元素
name[0] = 'Shirley' # 把下标0 的元素改成‘Shirley’

#查询  in / not in
if 'Angler' not in name_List
    print('Name available..')