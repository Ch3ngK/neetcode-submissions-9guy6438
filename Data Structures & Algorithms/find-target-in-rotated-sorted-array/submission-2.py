class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        l = 0
        r = len(nums) - 1

        while (l <= r):
            m = (l + r) // 2
            
            if nums[m] == target:
                res = m
                break

            if nums[m] >= nums[l]:
                if nums[m] > target and nums[l] <= target:
                    r = m - 1
                else: 
                    l = m + 1
            else:
                if nums[m] < target and nums[r] >= target:
                    l = m + 1
                else: 
                    r = m - 1
        return res 