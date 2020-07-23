'''
Input: an integer
Returns: an integer
'''

# Time complexity: O(n)
# Space complexity: O(n)
def eating_cookies(n, cache=None):
    # base cases
    if n < 0:
        return 0
    elif n == 0:
        return 1
    # check if the work has already been done
    # by looking in the cache
    elif cache and cache[n] > 0:
        # return the previously computed answer and don't recurse
        return cache[n]
    else:
        # might need to create our cache for the first time
        if cache is None:
            # initialize an empty list for a cache
            cache = [0] * (n + 1)
        # store the value of the recursive call expressions in our cache
        print("n - 1", eating_cookies(n - 1, cache), "n - 2", eating_cookies(n - 2, cache), "n - 3", eating_cookies(n - 3, cache))
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)

    return cache[n]

    # return solution


print("solution:", eating_cookies(3))

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    print(f"There are {eating_cookies(num_cookies)} cookies cm can eat")
