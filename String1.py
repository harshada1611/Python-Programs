# String


# input = 4A2B3C2D
# output = AAAACCCBBDD
# str = input('Enter str: ')
# output = ''
# for ch in str:
#     if ch.isalpha():
#         x = ch
#     else:
#         d = int(ch) 
#         output = output + x * d
# print(output)           


s = input("Enter string: ")
target = ""

for ch in s:
    if ch.isalpha():
        x = ch
    elif ch.isdigit():
        d = int(ch)
        target = target + x * d

output = ''.join(sorted(target))
print(output)