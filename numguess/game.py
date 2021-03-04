import random

user_name = input('Enter your name: ')

answer = random.randint(1,100)

#for debugging.
#print(user_name, answer)
print(answer)

guess = input('welcome {}. Please tell me the answer : '.format(user_name))

# for debugging.
print(answer,guess)
