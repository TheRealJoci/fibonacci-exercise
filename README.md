# Fibonacci exercise

## Project description

This exercise is meant to showcase the use of optimization techniques on the problem of generating the Fibonacci sequence.

Techniques showcased are used to improve the implied recursive method of generating the sequence. They are:

* Memoization
* Tabulation
* Generation

## Fibonacci sequence definition

The sequence is defined recursively:

$F_0 = 0$

$F_1 = 1$

$F_n = F_{n-1} + F_{n-2}$

And the sequence generated is:

$0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...$

## Timing the function execution

A simple decorator style wrapper was used to time the function execution in wall time terms.

```python
def stopwatch_iterative(func, iterations):
    def stopwatch_wrapper(function_input):
        time_sum = 0
        for _ in range(iterations):
            t1 = time()
            func(function_input)
            t2 = time()
            time_sum += t2 - t1
        print(
            f"Average execution time for {function_input}th fibonacci number over {iterations} iterations: {time_sum/iterations:.2f}s")
    return stopwatch_wrapper

# Execution
stopwatch_iterative(function, iterations)(function_input)
```

## Recursive approach

The recursive style definition in Python:

```python
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 2:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
```

Executing this function in our stopwatch outputs:

> Average execution time for 30th Fibonacci number over 10 iterations: 0.24s
>
> Average execution time for 35th Fibonacci number over 10 iterations: 2.67s
>
> Average execution time for 40th Fibonacci number over 10 iterations: 28.36s

We can see a big spike in execution time for our recursive implementation. The problem with this is that we keep having repeating recursive calls for the same parameters over and over again.

## Memoization approach

We can improve the execution time of our recursive function by implementing a cache that will store every nth Fibonacci number after the first time it is calculated, and just do a cache lookup every time the recursive function is called to find if the number was calculated before.

### The dictionary implementation

```python
fibonacci_cache = {0: 0, 1: 1}

def fibonacci_memo(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    else:
        value = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
        fibonacci_cache[n] = value
        return value
```

To make an accurate stopwatch measurement we need to reset the cache in between each iteration. If it wasn't for the benchmark cache would be very useful and should not be reset:

```python
if func.__name__ == 'fibonacci_memo':
    global fibonacci_cache
    fibonacci_cache = {0: 0, 1: 1}
```

The stopwatch output is:

> Average execution time for 995th Fibonacci number over 10 iterations: 0.000453s

As we see the function is blazing fast. The other problem that we run into is the recursive call limitation in Python which stops us from putting more then a 1000 recursive calls on the stack.

Even though modifying that limitation is possible it's not recommended therefore it's not a realistic solution to real world problems that we might face with using Python in the future.

### The decorator cache implementation

Using Python's *functools* module we can just use a build-in way that python handles cache. There are several options, to name a few: *cache* or *lru_cache* functions.

We can use mentioned functions as decorators to the already defined recursive implementation:

```python
@cache
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 2:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
```

The biggest problem with this implementation is that using a decorator puts a function on the stack and with that in a sense halves the built-in recursive call limit of Python.

## Tabulation approach
