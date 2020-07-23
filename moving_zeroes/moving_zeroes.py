'''
Input: a List of integers
Returns: a List of integers
'''


# Time complexity: O(n)
# Space complexity: O(1)
def moving_zeroes(arr):
    # j increments each time a non-zero integer is moved
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            # swap the non-integer zero with j
            if j != i:  # swap doesn't need to be made if j and i are the same
                arr[j], arr[i] = arr[i], arr[j]
            # increment so the next 0 has a spot
            j += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    # arr = [0, 3, 1, 0, -2]
    # arr = [1, 2, 3, 0, 4, 0, 0]
    # arr = [0, 3, 1, 0, 0, 2, 4]
    arr = [0, 0, 0, 2, 3, 4]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
