for i in range(1,100+1):
    if i %3 == 0 and i %5 == 0: print('피즈버즈')
    elif i %3 == 0 : print('FIZZ')
    elif i %5 ==0 : print('BUZZ')
    else: print(i)
