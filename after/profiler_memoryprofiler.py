from memory_profiler import profile
import time


@profile
def slow_function():
    time.sleep(2)
    total = 0
    for i in range(10000):
        total += i ** 2
    return total


@profile
def optimized_fast_function():
    return sum(i**2 for i in range(100))


@profile
def memory_intensive_function():
    total = 0
    for i in range(10000000):
        total += i ** 2
    return total


def main():
    slow_function()
    optimized_fast_function()
    memory_intensive_function()


if __name__ == "__main__":
    main()