if input('Welcome. Please type start to begin the game:') == 'start':
        print('Let\'s begin the game.\nYou must choose two numbers and provide a guess for which number is randomly generated.\nA precondition is that the first number must be less than the second value.')
        num1 = int(input('Choose the first number:'))
        num2 = int(input('Choose the second number:'))
        if not num1 < num2:
                print('You have not followed the precondition. Please try again from the beginning.')
        print('You have selected the numbers:',num1,',',num2,'thank you.')
        import random
        num = random.randint(num1,num2)
        tries = 1
        question1 = 'Please guess what number has been randomly generated.\nYour guess:'
        guess = int(input(question1))
        if num == guess:
                print('Congratulations, you guessed correctly on your first try!')
        else:
                while num != guess:
                        print('Your guess is incorrect, please try again.')
                        guess = int(input('Your guess:'))
                        tries += 1
                        if guess == num:
                                print('Correct, it took you', tries, 'tries to guess the correct answer.')
                                break
                        else:
                                print('Your guess is incorrect, please try again.')
