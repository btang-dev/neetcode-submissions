class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} 
        longest = 0
        
        l = 0
        for r in range(len(s)):
            # increment the count based on the character present
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # not valid when the number of replacements is bigger than k
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            # update longest
            longest = max(longest, r - l + 1)
        return longest