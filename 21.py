# 局部变量 variable
a = 100

def test():
    global a  # 允许在一个函数里修改全局变量
    a = 33

def test1():
    pass

test() #必须调用这个函数运行，变量值才会被改变
print(a)


# -------------------student information system--------------
# -----------------------------------------------------------
# methods:

#student_List = [{'Name':'George','Age':27,'Phone':5112100},{'Name':'John','Age':25,'Phone':04015415}];
student_List = [{'Name': 'John', 'Phone': '0432550853', 'Age': '27'}] # 建一个列表，把字典放进去

'''start menu'''
def start_menu():
    print('--------Student List--------')
    print('1: Add a new student')
    print('2: Delete a student')
    print('3: Edit a student')
    print('4: Search a student')
    print('5: Sow all student')
    print('6: Exit')
    print('----------------------------')

'''add a new student'''
def add_student():
    global student_List
    new_Name = input('please enter name: ')
    new_Age = input('please enter age: ')
    new_Phone = input('please enter phone number: ')
    new_Student = {}
    new_Student['Name'] = new_Name
    new_Student['Age'] = new_Age
    new_Student['Phone'] = new_Phone
    student_List.append(new_Student)

def search_student(): # search a student
    global student_List
    find_Name = input('please enter a name for search')
    find_flag = 0 # 默认表示没有找到
    for temp in student_List:
        if find_Name == temp['Name']:
            print('find student')
            print('Name\tAge\tPhone') #格式
            print('%s\t%s\t%s'%(temp['Name'],temp['Age'],temp['Phone']))
            find_flag = 1;
            break
    if find_flag == 0:
        print('no student match')
       

def show_all_info():  #show all infor
    global student_List # 如果全局变量是字典或者列表，没有global声明也不影响 
    print('Name\tAge\tPhone') #格式
    for temp in student_List: #遍历 student_List 存进 temp 打印出来
        print('%s\t%s\t%s'%(temp['Name'],temp['Age'],temp['Phone']))




def main():
#----------------start------------------
    
    start_menu()
    while True:
        
        select = int(input('please select a function: '))
        if select == 1:
            add_student()

        elif select == 2:
            pass

        elif select == 3:
            print(search_student)

        elif select == 4:
            search_student()

        elif select == 5:
            show_all_info()
        
        elif select == 6:
            print('good bye~~')
            break
        else:
            print('error, please try again')


main()