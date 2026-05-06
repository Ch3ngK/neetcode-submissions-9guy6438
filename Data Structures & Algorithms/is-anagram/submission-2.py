class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabets1 = [0] * 26
        alphabets2 = [0] * 26
        for i in range(len(s)):
            curr = ord(s[i]) - ord('a')
            alphabets1[curr] += 1

        for j in range(len(t)):
            curr = ord(t[j]) - ord('a')
            alphabets2[curr] += 1

        return alphabets1 == alphabets2