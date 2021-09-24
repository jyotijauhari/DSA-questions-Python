# 744. Find Smallest Letter Greater Than Target

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters) - 1
        
        if ord(target) >= ord(letters[end]):
            return letters[start]
        
        while start <= end:
            mid = (start + end)//2
            
            if ord(letters[mid]) == ord(target):
                start = mid + 1
            elif ord(letters[mid]) >= ord(target):
                end  = mid - 1
            else:
                start = mid + 1
        return letters[start]
