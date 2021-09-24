#  brute force - using set, 
# tc -  O(N^2) as intersection is O(N) 
# i.e min(len(front),len(back)) and O(N) as run intersection n times
# space - string are immutable so extra space

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        sizes = []
        while s:
            i = 1
            while set(s[:i]) & set(s[i:]):
                i += 1
            sizes.append(i)
            s = s[i:]
        return sizes
    
# optimised
# O(n) time , O(n) - space

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        """
              0 1 2 3 4 5 6 7 8
              a b c a b c e f g
        i     i i i i i i i i i
        start s           s s s
        end         e e e e e e
        output          6 1 1 1
        """
        last = {c:i for i,c in enumerate(S)}
        start = end = 0
        output = []
        for i,c in enumerate(S):
            end = max(end,last[c])
            if i == end:
                output.append(end-start+1)
                start = i + 1
        return output
