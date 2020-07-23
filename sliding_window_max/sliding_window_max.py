'''
Input: a List of integers as well as an integer `k`
representing the size of the sliding window
Returns: a List of integers
'''


# Time complexity: O(nk)
# Space complexity: O(n)
def sliding_window_max(nums, k):
    output = []

    for i in range(len(nums) - (k - 1)):
        max = nums[i]

        for x in range(k):
            if nums[i + x] > max:
                max = nums[i + x]

        output.append(max)

    return output


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 2

    print(f"Output: {sliding_window_max(arr, k)}")
