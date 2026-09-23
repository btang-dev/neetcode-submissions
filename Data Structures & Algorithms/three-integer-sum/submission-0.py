class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Can't have duplicates
        # Has to equal to 0
        # Brute force: triple loop to get a combination of three numbers to equal to 0
        
        #Optimal:
        #Sort the array and if there is a duplicate, skip it.
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

        #Once we find our first value, refer back to two sum II
        #use a left and right pointer
            left, right = i + 1, len(nums) - 1

        #if the current sum is greater than the target value, move right to the left, then move left to right if still too small
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                   left += 1
                else:
                    res.append([a, nums[left], nums[right]])  
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                       left += 1
        return res

