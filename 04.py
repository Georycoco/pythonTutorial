age = input('Please enter your age: '); # all data retrived by input will be a string type;
age_Num = int(age); # transfer '20' to 20;
income = 5000;
name = 'George';
address = 'UNIT 1/Blackburn VIC';

if age_Num >= 18:      # not equal to: !=  or  <>  
    print('I can go clubing~~');
else:
    print('Oh, you are too young to enjoyment');

print('Name is: %s, Age: %s, Income: %s, Address: %s'%(age_Num, income, name, address));

print('='*20);
print(2*2);
print(2**3);
print('A'*10);
print('OMG ' *5);