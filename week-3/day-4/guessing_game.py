from random import randint

number_to_guess = randint(0, 100)
number_of_guesses = 6

def get_integer():
    num = int(input('Enter an integer: '))
    return num

while number_of_guesses > 0:
    try:
        number = get_integer()

    except ValueError:
        print('You entered a wrong value.')

    else:
        if number == number_to_guess:
            print('Yolo')
            break

        elif number > number_to_guess:
            print('No, the my number is less')
            number_of_guesses -= 1

        else:
            print('No, the my number is bigger')
            number_of_guesses -= 1

if number_of_guesses == 0:
    print('You are lame! My number was', number_to_guess)
