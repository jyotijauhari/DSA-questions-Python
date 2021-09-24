# https://leetcode.com/problems/crawler-log-folder
# time and space - O(n)

class Solution:
    
    def minOperations(self, logs: List[str]) -> int:   
        stack = []
        
        for word in logs:
            
            if word == "../" and len(stack) > 0:
                stack.pop()
                
            elif word == "./":
                continue
                
            elif word != "../" and word != "./":
                stack.append(word)
                
        return len(stack)