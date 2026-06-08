#NestedTernary_max.py

a = int(input('Enter first value: '))
b = int(input('Enter second value: '))
c = int(input('Enter thoird value: '))
max = a if a>b and a>c else b if b>c else c 
print('Maximum value is: ',max)