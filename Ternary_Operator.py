#Ternary_Operator

#Minimum value
# a = int(input('Enter  value for a: '))
# b = int(input('Enter value for b: '))
# min = a if a<b else b
# print('The minimum value is:',min)


#Maximun value
a = int(input('Enter value for a: '))
b = int(input('Enter value for b: '))
c = int(input('Enter value for c: '))
max = a if a>b and a>c else b if b>c else c
print('The maximum value is: ',max)