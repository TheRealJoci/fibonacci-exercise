from time import time


def stopwatch(func):
    def stopwatch_wrapper(function_input):
        t1 = time()
        func(function_input)
        t2 = time()
        print("{:.6f}s".format(t2 - t1))
    return stopwatch_wrapper


def stopwatch_iterative(func, iterations):
    def stopwatch_wrapper(function_input):
        time_sum = 0
        for _ in range(iterations):
            if func.__name__ == 'fibonacci_memo':
                global fibonacci_cache
                fibonacci_cache = {0: 0, 1: 1}
            t1 = time()
            func(function_input)
            t2 = time()
            time_sum += t2 - t1
        print(
            f"Average execution time for {function_input}th Fibonacci number over {iterations} iterations: {time_sum/iterations:.6f}s")
    return stopwatch_wrapper


def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


fibonacci_cache = {0: 0, 1: 1}


def fibonacci_memo(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    else:
        value = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
        fibonacci_cache[n] = value
        return value


# use functions after this comment
