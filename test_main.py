

from main import rand_generator


def test_rand_generator():
    for _ in range(100):
        result = rand_generator(1, 10)
        assert 1 <= result <= 10, f"Value {result} not in range"
    return
