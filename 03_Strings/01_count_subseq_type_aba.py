'''

type - GFG
ip - GFGFG
op - 4

'''

#method 1
for _ in range(int(input())):
    s = input()
    a = s.count('G')
    x = 0
    ans = 0
    n = len(s)
    for i in range(n):
        if s[i] == 'F':
            ans += x *(a-x)
        else:
            x+=1
    print(ans)

#method 2
# def countsubseq(s):
#     cntG = 0
#     cntF = 0
#     C = 0
#     result = 0
#
#     for i in s:
#         if i == "G":
#             cntG += 1
#             result += C
#         if i == "F":
#             cntF += 1
#             C += cntG
#     return result
#
# #print(countsubseq("GFGFG"))
# print(countsubseq("FFGFF"))

