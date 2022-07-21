"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Constraints:

-2^31 <= x <= 2^31 - 1
"""
def is_palindrome(x):
    assert x >= -2**31 , 'X must be greater than or equal -2^31'
    assert x <= 2**31 - 1 , 'X must be less than or equal -2^31'
    assert type(x) is int, 'X must be an integer'
    y = ''
    for i in reversed(list(str(abs(x)))):
        y += i
    y = int(y)
    return x == y