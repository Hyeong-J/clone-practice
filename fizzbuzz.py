#<<<<<<< HEAD
#for i in range(1,300+1):
#    if i %3 == 0 and i %5 == 0: print('fizzbuzz')
#    elif i %3 == 0 : print('fizz')
#    elif i %5 ==0 : print('buzz')
#    else: print(i)
#=======
print(['fizzbuzz' if i%3 ==0 and i%5 ==0 
    else 'fizz' if i%3==0 
    else 'buzz' if i%5==0 
    else i
    for i in range(1,300+1)])
#>>>>>>> fb-listcomp
