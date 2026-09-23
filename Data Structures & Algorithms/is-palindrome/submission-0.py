class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""

        for constant in s:
            if constant.isalnum():
                newString += constant.lower()
        return newString == newString[::-1]