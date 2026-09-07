class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = [0] * 26
        arr2 = [0] * 26

        for i in range(len(s)):
            cur = ord(s[i]) - ord('a')
            arr1[cur] += 1
        for j in range(len(t)):
            cur = ord(t[j]) - ord('a')
            arr2[cur] += 1

        if arr1 == arr2:
            return True
        return False