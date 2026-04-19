#3783. Mirror Distance of an Integer
class Solution:
    def mirrorDistance(self, n: int) -> int:
        karibasu = str(n)

        reversed_karibasu = karibasu[::-1]  # Reverse the string

        reversed_n = int(reversed_karibasu) #again it will convert to integer

        return abs(n-reversed_n) # Return absolute difference666666

       