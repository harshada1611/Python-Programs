# Sort_AlphbetsAdDigits
# str = B3D1C2Z0
str = input('Enter string: ')
digits = []
alphabets = []
for ch in str:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)
output = ''.join(sorted(alphabets)+sorted(digits))
print(output)            