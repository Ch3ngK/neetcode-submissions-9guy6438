class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 0(26*n) approach
        count = {}
        l = 0
        maximum = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            # r - l + 1 refers to current window length
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            maximum = max(maximum, r - l + 1)
        return maximum

            