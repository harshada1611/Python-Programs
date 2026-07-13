num = int(input('Enter num: '))
if num <= 1:
    print('Not prime number')
else:
    is_prime = True
    for i in range(2, num):
        if(num % i ==0):
            is_prime = False            
    if is_prime == True:
        print('Prime num')
    else:
        print('Not prime number')    

    

            

