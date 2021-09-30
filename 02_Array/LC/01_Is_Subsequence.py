# LC 392

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        if n == 0:
            return True
        count = 0
        for char in t:
            if char == s[count]:
                count += 1
            if count == n:
                return True
        return False
            
