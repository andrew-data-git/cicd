

from main import rand_generator, check_if_even


def test_rand_generator():
    for _ in range(100):
        result = rand_generator(1, 10)
        assert 1 <= result <= 10, f"Value {result} not in range"


def test_check_is_even():
    odds = [1, 3, -999]
    evens = [0, 2, 40, -6]

    for number in odds:
        assert check_if_even(number) == 'ODD'

    for number in evens:
        assert check_if_even(number) == 'EVEN'
