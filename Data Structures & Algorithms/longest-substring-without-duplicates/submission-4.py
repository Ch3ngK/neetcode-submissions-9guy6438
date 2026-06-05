class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charSet = set()
        length = len(s)
        maximum = 0
        for r in range(length):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            maximum = max(maximum, r - l + 1)
        
        return maximum

