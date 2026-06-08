#Smallest_three

a= int(input('Enter first num: '))
b= int(input('Enter second num: '))
c= int(input('Enter third num: '))
if a<b and a<c:
    print('smallest num is: ',a)
elif b<a and b<c:
    print('smallest num is: ',b)
else:
    print('smallest num is: ',c)
