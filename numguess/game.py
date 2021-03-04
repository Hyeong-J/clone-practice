import random

user_name = input('Enter your name: ')

answer = random.randint(1,100)

#for debugging.
#print(user_name, answer)
print(answer)

guess = int(input('welcome {}. Please tell me the answer : '.format(user_name)))

# for debugging.
print(answer,guess)

#if guess==answer:
#    print('Correct!!')
#else:
#    print('Wrong!!! The answer was {} try again'.format(answer))
count = 0
while guess!=answer:
    count+=1
    if count ==3:
        print('You fail to correct the number')
    elif print('Correct')
