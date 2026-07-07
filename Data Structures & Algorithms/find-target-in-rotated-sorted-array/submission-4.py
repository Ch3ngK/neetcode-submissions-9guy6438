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

            #Left-sorted segment
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else: 
                    r = m - 1
            
            # Right-sorted segment
            else:
                if target < nums[m] or target > nums[r]: 
                    r = m - 1
                else: 
                    l = m + 1
        return res 