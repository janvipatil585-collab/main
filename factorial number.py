num=int(input('enter your number:'))
factorial=1
if num>0:
    for i in range(1,num+1):
        factorial=factorial*i
        print('factorial of number is:',factorial)
elif num==0:
    print('factorial of 0 is 1')
else:
    print('factorial of negative not possible')
        