 #9. Palindrome Number

#palindrome number is a number it reamins same when we reverse it

#x = 'hilih'

#if x == x[::-1]:
 #   print('True')

# above works for test

class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Negative numbers are never palindromes
        if x < 0:
            return False

        # Save the original number
        original = x

        # Variable to store the reversed number
        reverse = 0

        # Reverse the digits
        while x > 0:

            # Take the last digit and add it to reverse
            reverse = (reverse * 10) + (x % 10)

            # Remove the last digit from x
            x = x // 10

        # Compare original and reversed numbers
        if original == reverse:
            return True
        else:
            return False