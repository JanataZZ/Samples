
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
    return False

has_lucky_number = has_lucky_number([1,3,9,15,21])

if has_lucky_number == True: 
    print('Yes, there is at least 1 lucky number')
else:
    print('The list does not contain lucky numbers')    