class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        maximum = 0
        for i in range(length):
            charSet = set()
            for j in range(i, length):
                if (s[j] in charSet):
                    break
                
                charSet.add(s[j])
                maximum = max(maximum, j - i + 1)
        return maximum