class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            currentSum = numbers[l] + numbers[r] # assign the current sum to l + r
            if currentSum > target: # move the right pointer to the left once
                r -= 1
            elif currentSum < target: # move the left point to the right once
                l += 1
            else:
                return [l + 1, r + 1] # return the list if the target is met by l and r
        return [l, r] # return the list outside the while loop
        