class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        needTable, haveTable = {}, {}

        # Initialise the needTable
        for c in t:
            needTable[c] = 1 + needTable.get(c, 0)  
        
        have = 0
        need = len(needTable)
        l = 0 # left pointer
        res, resLen = [-1, -1], float("infinity")
        for r in range(len(s)): 
            c = s[r] 
            haveTable[c] = 1 + haveTable.get(c, 0)

            if c in needTable and haveTable[c] == needTable[c]:
                have += 1

            while need == have:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                
                left_char = s[l]
                haveTable[left_char] -= 1
                if left_char in needTable and haveTable[left_char] < needTable[left_char]:
                    have -= 1
                    
                l += 1

        l, r = res
        return s[l:r+1]

