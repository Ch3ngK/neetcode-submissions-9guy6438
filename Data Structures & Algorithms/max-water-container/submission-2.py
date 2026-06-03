class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        length = len(heights)

        for i in range(length):
            for j in range(i + 1, length):
                amount = (j - i) * min(heights[i], heights[j])
                maximum = max(maximum, amount)

        return maximum