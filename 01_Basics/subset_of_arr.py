# method 1 - bitmasking
#Bitmasking to find subset

s = [1,2,3]
n = len(s)

size = pow(2,n)
ans = []
# 0 to 7
for i in range(size):
    subset = []
    # checking idx position
    for j in range(0,n):
        if(i & (1<<j)):
            subset.append(s[j])
    ans.append(subset)
print(ans)

# using recursion
def subseq(nums, ans, curr, index):
    if index > len(nums):
        return
    ans.append(curr[:])
    for i in range(index, len(nums)):
        if nums[i] not in curr:
            curr.append(nums[i])
            subseq(nums, ans, curr, i)
            curr.pop()
    return
        


nums = [1,2,3]
ans = []
curr = []
index = 0
subseq(nums, ans, curr, index)
print(ans)
