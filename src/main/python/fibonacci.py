def fibonacci_recursion(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)


def fibonacci(n):
    fib_series = {0: 0, 1: 1}
    i = 2
    while i <= n:
        fib_series[i] = fib_series[i-1] + fib_series[i-2]
        i = i+1
    return fib_series.get(n)


def main():
    result = fibonacci_recursion(9)
    result = fibonacci(9)

import pytest

class TestClass:
    def test_fibonacci_recursion(self):
        assert 0 == fibonacci_recursion(0)
        assert 1 == fibonacci_recursion(1)
        assert 1 == fibonacci_recursion(2)
        assert 2 == fibonacci_recursion(3)
        assert 3 == fibonacci_recursion(4)
        assert 5 == fibonacci_recursion(5)
        assert 8 == fibonacci_recursion(6)
        assert 13 == fibonacci_recursion(7)
        assert 21 == fibonacci_recursion(8)
        assert 34 == fibonacci_recursion(9)

    def test_fibonacci(self):
        assert 0 == fibonacci(0)
        assert 1 == fibonacci(1)
        assert 1 == fibonacci(2)
        assert 2 == fibonacci(3)
        assert 3 == fibonacci(4)
        assert 5 == fibonacci(5)
        assert 8 == fibonacci(6)
        assert 13 == fibonacci(7)
        assert 21 == fibonacci(8)
        assert 34 == fibonacci(9)


if __name__ == "__main__":
    main()
    print(pytest.main(["-x", 'fibonacci.py']))
    print("Hello {:4}".format('pad'))
    print("Hello [{:5}] [{:^5}] [{:>5}]".format('pad', 'pad', 'pad'))
