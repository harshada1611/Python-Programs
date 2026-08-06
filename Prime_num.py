num = int(input('Enter num: '))
if num <=1:
    print('Not prime num')
else:
    is_prime = True
    for i in range(2, num):
        if num % i==0:
            is_prime =False
            break
if is_prime == True:
    print('Yes prime')
else:
    print('Not prime')            