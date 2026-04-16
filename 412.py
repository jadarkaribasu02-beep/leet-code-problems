# 412. Fizz Buzz
class Solution:
   
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []  # Create an empty list to store the results

        # Loop through numbers from 1 to n (inclusive)
        for i in range(1, n + 1):

            # If the number is divisible by both 3 and 5
            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")  # Add "FizzBuzz" to the list

            # If the number is divisible only by 3
            elif i % 3 == 0:
                ans.append("Fizz")  # Add "Fizz" to the list

            # If the number is divisible only by 5
            elif i % 5 == 0:
                ans.append("Buzz")  # Add "Buzz" to the list

            # If the number is not divisible by 3 or 5
            else:
                ans.append(str(i))  # Add the number itself (as a string)

        # Return the final list of results
        return ans
