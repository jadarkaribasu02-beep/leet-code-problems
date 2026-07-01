class Solution:
    def sumOfMultiples(self, n: int) -> int:
        new = []
        
        # 1. Loop from 1 to n inclusive
        for i in range(1, n + 1):
            # 2. Check if divisible by 3, 5, or 7
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                new.append(i)
                
        # 3. Return the built-in sum of the list
        return sum(new)
