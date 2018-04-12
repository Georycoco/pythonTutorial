# student list table

print('--------Student List--------')
print('1: Add a new student')
print('2: Delete a student')
print('3: Edit a student')
print('4: View a student')
print('5: Exit')
print('----------------------------')
student_List = [];
name = ['George','John','Tim'] # add new names

while True:
    
    select = int(input('Please select a function: '))
    if select == 1:
        new_Name = input('please enter a name: ')
        name.append(new_Name)
        print(name)
    elif select == 2:
        delete_Name = input('enter the name to delete: ')
        name.remove(delete_Name)
        print(name)
    elif select == 3:
        old_Name = input('please enter the name to edit: ')
        edit_Name = input('please enter new name: ')
        p = name.index(old_Name)  # p = old_Name 元素在 name 列表中的位置
        name[p] = edit_Name
        print(name)
    elif select == 4:
        find_Name = input('please input the name for look up: ')
        if find_Name in name:
            print('student is in list')
        else:
            print('no student match')
    elif select == 5:
        print('Good Bye~~')
        break;
    else:
        print('Unknow input, please try again')




