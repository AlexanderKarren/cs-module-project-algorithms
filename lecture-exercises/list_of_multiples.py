# List of Multiples Plan

# Iterate up to length + 1 and multiply i by the passed in num.

# Add these values to a list.

def list_of_multiples(num, length):
    return [num * x for x in range(1, length + 1)]

print(list_of_multiples(17, 6))
