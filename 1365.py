#1365. How Many Numbers Are Smaller Than the Current Number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        # Create an empty list to store the answers
        ka = []

        # Take each number from the list one by one
        for i in nums:

            # Count of numbers smaller than the current number
            count = 0

            # Compare the current number with every number in the list
            for j in nums:

                # If another number is smaller than the current number
                if j < i:
                    count += 1      # Increase the count

            # After checking all numbers, store the count
            ka.append(count)

        # Return the final list containing all counts
        return ka