# Time complexity: O(n)
# Space complexity: O(1)
def divides_self(num):
    for digit in str(num):
        if int(digit) <= 0 or num % int(digit) > 0:
            return False
    
    return True

print(divides_self(128))
print(divides_self(12))
print(divides_self(120))
 
# Plan
# What happens in num equals 0
# if num equals 0
    # return False

# loop through each digit in num
    # if digit does not evenly divide into num or if digit equals 0
        # return False

# Going to need modulo (even division)
# May need split
# Need method for isolating each digit in the num