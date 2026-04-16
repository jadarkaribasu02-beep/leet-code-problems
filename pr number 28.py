
#28. Find the Index of the First Occurrence in a String

# explanation
# haystack: str → the main string we are searching inside.
# needle: str → the substring we want to find.
# haystack.find(needle) is a built-in Python string method.



class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        return haystack.find(needle)
        