from src.intro import max, fizBuzz


def test_max():
    assert max(1, 2) == 2
    assert max(2, 1) == 2


class TestFizBuzz:
    # it sould return FizzBuzz if arg is divisible by 3 and 5
    def test_return_fizzbuzz(self):
        assert fizBuzz(15) == "FizzBuzz"

    def test_fizz_only_divisible_by_3(self):
        assert fizBuzz(21) == "Fizz"

    def test_buzz_only_divisible_by_5(self):
        assert fizBuzz(10) == "Buzz"
        assert fizBuzz(5) == "Buzz"