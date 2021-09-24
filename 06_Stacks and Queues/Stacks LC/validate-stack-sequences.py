# https://leetcode.com/problems/validate-stack-sequences

# Initialize am empty stack,
# iterate and push elements from pushed one by one.
# Each time, we'll try to pop the elements from as many as possibile popped.
# In the end, we we'll check if stack is empty.

# Time O(N)
# Space O(N)

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        i = 0           #for traversing popped list
        
        for ele in pushed:
            
            if not pushed and not popped:
                return True
            
            stack.append(ele)
            
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
                
        return len(pushed) == i
    
        # if stack:
        #     return False
        # else:
        #     return True

#another approach        
# using pushed as the stack.
# This solution will take O(1) extra space,
# though it also changed the input.

# Time O(N)
# extra Space O(1),   O(N) modified space

'''
    def validateStackSequences(self, pushed, popped):
        i = j = 0
        for x in pushed:
            pushed[i] = x
            while i >= 0 and pushed[i] == popped[j]:
                i, j = i - 1, j + 1
            i += 1
        return i == 0
'''
