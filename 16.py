# student information 

print('--------Student List--------')
print('1: Add a new student')
print('2: Delete a student')
print('3: Edit a student')
print('4: Search a student')
print('5: Sow all student')
print('6: Exit')
print('----------------------------')

#student_List = [{'Name':'George','Age':27,'Phone':5112100},{'Name':'John','Age':25,'Phone':04015415}];
student_List = [{'Name': 'John', 'Phone': '0432550853', 'Age': '27'}] # 建一个列表，把字典放进去

while True:
    
    select = int(input('Please select a function: '))
    if select == 1:
        new_Name = input('please enter name: ')
        new_Age = input('please enter age: ')
        new_Phone = input('please enter phone number: ')
        new_Student = {}
        new_Student['Name'] = new_Name
        new_Student['Age'] = new_Age
        new_Student['Phone'] = new_Phone
        student_List.append(new_Student)

        #print(student_List) for test
    elif select == 3:
        print(student_List)


    elif select == 2:
        delete_Name = input('enter name to delete')
        for temp in student_List:
            if delete_Name == temp['Name']:
                pass
                


        print(student_List)


    elif select == 4: # search a student
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

    elif select == 5:
        print('Name\tAge\tPhone') #格式
        for temp in student_List: #遍历 student_List 存进 temp 打印出来
            
            print('%s\t%s\t%s'%(temp['Name'],temp['Age'],temp['Phone']))

    elif select == 6:
        print('Good Bye~~')
        break;
    else:
        print('Unknow input, please try again')
    print('')
