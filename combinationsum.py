class Solution(object):
    def combinationSum(self, candidates, target):
        self.res=[]
        
        self.recur( candidates, target, [])
        return self.res
    
    def recur(self, candidates, target, sublist):
        
        if target<0:
            return 
        if target == 0:
            self.res.append(sublist)
            return
        
        for i in range(len(candidates)):
            self.recur(candidates[i:], target - candidates[i], sublist+[candidates[i]])
            #sublist.pop()
            #sublist.pop(candidates[i])
