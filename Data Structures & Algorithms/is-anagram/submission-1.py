class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## using all of the characters of a string with the same exact strings
        ## two variables and if they use the same characters, return true, otherwise false
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) ## 0 is the default value, get gets the key of the hashmap, if it doens't exist return 0
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT