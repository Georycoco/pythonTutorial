# student information 

print('--------Student List--------')
print('1: Add a new student')
print('2: Delete a student')
print('3: Edit a student')
print('4: View a student')
print('5: Exit')
print('----------------------------')

#student_List = [{'Name':'George','Age':27,'Phone':5112100},{'Name':'John','Age':25,'Phone':04015415}];
student_List = [{'Name': 'John', 'PHone': '0432550853', 'Age': '27'}] # 建一个列表，把字典放进去

while True:
    
    select = int(input('Please select a function: '))
    if select == 1:
        new_Name = input('please enter name: ')
        new_Age = input('please enter age: ')
        new_Phone = input('please enter phone number: ')
        new_Student = {}
        new_Student['Name'] = new_Name
        new_Student['Age'] = new_Age
        new_Student['PHone'] = new_Phone
        student_List.append(new_Student)
        print(student_List)

    elif select == 2:
       
        print(student_List)

    elif select == 3:
       
        print(student_List)

    elif select == 4:
        

        
        if find_Name in student_List:
            print('student is in list')
        else:
            print('no student match')

    elif select == 5:
        print('Good Bye~~')
        break;
    else:
        print('Unknow input, please try again')
    print('')
