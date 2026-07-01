class Solution:
    def addDigits(self, num: int) -> int:

        while num >= 10:      # Repeat until one digit remains
            tota = 0

            while num > 0:
                digit = num % 10   # Get last digit
                tota += digit     # Add it
                num //= 10         # Remove last digit

            num = tota

        return num