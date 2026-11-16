class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # if mid is on the target, return mid
            if nums[mid] == target:
                return mid
            # if the target is higher than mid, move the left pointer forward
            elif nums[mid] < target:
                l = mid + 1
            # if the target is less than the mid, move the right pointer backwards
            else:
                r = mid - 1
        return -1