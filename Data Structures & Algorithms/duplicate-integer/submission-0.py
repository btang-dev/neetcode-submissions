class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ## if there is a duplicate return true
        ## otherwise return false
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        