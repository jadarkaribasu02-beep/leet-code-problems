class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(char.lower() for char in s if char.isalnum())
        k = clean_s[::-1]
        if k == clean_s:
            return True
        else:
            return False    
