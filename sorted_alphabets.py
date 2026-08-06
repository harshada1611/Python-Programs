# sorted_alphabets.py

str = input('Enter string with digits: ')
output = ''
for ch in str:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        output = output + x * d
print(output)            

