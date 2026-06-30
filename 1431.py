#Kids With the Greatest Number of Candies


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        maxcandy = max(candies)
        ans = []

        for i in candies:
            if (i + extraCandies)>=maxcandy:
                ans.append(True)

            else:
                ans.append(False)

        return ans    
           
        # find max then add extra candies if condition is true then return True else False