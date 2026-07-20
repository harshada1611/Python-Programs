#Alternate two strings

s1 =input('Enter s1 string: ')
s2 =input('Enter s2 string: ')
i=0
j=0
output= ''
while i<len(s1) or i<len(s2):
    if i<len(s1):
        output = output + s1[i]
        i =i+1
    if j<len(s2):
        output = output + s2[j]
        j = j+1
print(output)    
