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
            arr[j], arr[i] = arr[i], arr[j]
            j += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")