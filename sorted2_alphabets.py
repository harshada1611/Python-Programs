# sorted2_alphabets.py

str = input('Enter string with digits: ')
target = ''
for ch in str:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        target = target + x * d
output = ''.join(sorted(target))
print(output)            

