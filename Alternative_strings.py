# Alternative strings
str1 = input('Enter string1: ')
str2 = input('Enter string: ')
output = ''
i = 0
j = 0 
while i<len(str1) or j <len(str2):
    if i<len(str1):
        output = output + str1[i]
        i = i+1
    if j<len(str2):
        output = output + str2[j]
        j = j+1
print('The alternative string is:',output)            

