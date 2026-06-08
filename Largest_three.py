#Largest_three

a= int(input('Enter first num: '))
b= int(input('Enter second num: '))
c= int(input('Enter third num: '))
if a>b and a>c:
    print('Largest num is: ',a)
elif b>a and b>c:
    print('Largest num is: ',b)
else:
    print('Largest num is: ',c)
