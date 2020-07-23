# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
def fib(n, cache=None):
    if n < 0:
        raise IndexError(
            'Index was negative. '
            'No such thing as a negative index in a series.'
        )
    elif n in [0, 1]:
        # base cases
        return n
    elif cache and cache[n]:
        return cache[n]
    else:
        if cache is None:
            cache = [0] * (n + 1)
        cache[n] = fib(n - 1, cache) + fib(n - 2, cache)
    print("computing fib(%i)" % n)
    return cache[n]


# def fib(n):
#     fibs = [0, 1]
#     count = 1
#     while count < n:
#         fibs.append((fibs[count] + fibs[count - 1]))
#         count += 1
#     return fibs[n]


print("solution:", fib(4))
