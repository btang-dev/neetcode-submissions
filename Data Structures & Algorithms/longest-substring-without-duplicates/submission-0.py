class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        counter: dict[str, int] = defaultdict(int)
        for r in range (len(s)):
            # go through each character while ending the right pointer of the window
            counter[s[r]] += 1

            #theres a duplicate
            while counter[s[r]] > 1:
                counter[s[l]] -= 1 # basically removing the duplicate letter at the start
                l += 1 # then moving the window from the left to the right once
            longest = max(longest, r - l + 1)
        return longest

