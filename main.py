

import random


def rand_generator(min, max):
    return random.randint(min, max)

def check_if_even(number):
    if number % 2 == 0:
        return 'EVEN'
    else:
        return 'ODD'


if __name__ == '__main__':
    value = rand_generator(1, 10)
    print(f'Your random number between 1 and 10 is... {value}')
    print(f'..and that is an {check_if_even(value)} number.')