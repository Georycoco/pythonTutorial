# 读写文件
f = open('text.txt','w')  # w 表示只读
f.write('Hello World')
f.flush()
f.close()

'''
fname = input('please enter file name: ')
file_read = open(fname,'r')  # r 可以不用写，如果没有默认为 r

#new_fname = 'Copy'+fname
#file_write = open(new_fname,'w')

p = fname.rfind('.')
new_fname = fname[0:p] + '[Copy]' + fname[p:]

file_write = open(new_fname,'w')

content = file_read.read()
file_write.write(content)

file_read.close()
file_write.close()
'''

#实际工作中如果几个G的文件，用read()会卡顿甚至奔溃，必须一点点读写 

fname = input('please enter file name: ')
file_read = open(fname,'r')  # r 可以不用写，如果没有默认为 r

p = fname.rfind('.')
new_fname = fname[0:p] + '[Copy]' + fname[p:]

file_write = open(new_fname,'w')

while True:
    content = file_read.read(1024) #每次只读1024kb的量 
    if len(content) == 0:
        break
    file_write.write(content)

file_read.close()


