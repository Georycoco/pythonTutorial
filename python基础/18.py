# 函数定义，调用


def start_Menu():
    print('--------Student List--------')
    print('1: Add a new student')
    print('2: Delete a student')
    print('3: Edit a student')
    print('4: Search a student')
    print('5: Sow all student')
    print('6: Exit')
    print('----------------------------')

def print_Triangle():
    
    i = 1;
    j = 1;
    while i <= 6:
        while j <= i:
            print('*'*j);
            j += 1;
        i += 1;
    print('end~~');

start_Menu()
print_Triangle()

