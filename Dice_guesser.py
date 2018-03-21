import random
num = random.randint(1,6)
guess = input('Please guess a number between 1 and 6')
int_guess = int(guess)
if num == int_guess:
    print('You are correct!')
while num != int_guess:
    int_guess = int(input('Please guess a number between 1 and 6'))
    if int_guess == num:
        print('You are correct!')
        break
    else:
        print('Please try again')
