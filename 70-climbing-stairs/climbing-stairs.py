class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 1,1
        for num in range(n):
            a,b = b,a+b 
            
        return a    

