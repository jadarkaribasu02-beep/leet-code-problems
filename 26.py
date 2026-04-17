# 26.remove duplicates from sorted array


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Convert to set to remove duplicates, then back to list
        nums[:] = list(set(nums))  # overwrite nums in place
        nums.sort()  # optional: keep elements sorted if required

        return len(nums)  # return the new length
