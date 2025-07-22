import random

def rand_generator(min, max):
    return random.randint(min,max)


if __name__ == '__main__':
    value = rand_generator(1,10)
    print(f'Your random number between 1 and 10 is... {value}')
