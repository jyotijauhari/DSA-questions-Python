'''
ip - "abcbdbebfb" ,b,x
op - axcxdxexfx

[hint - traversing reverse and replacing if found]
'''

def replacechar(s, r1, r2):
    if len(s) == 0:
        return s
    smallOutput = replacechar(s[1:], r1, r2)
    if s[0] == r1:
        return r2 + smallOutput
    else:
        return s[0] + smallOutput



s = "abcbdbebfb"
r1 = 'b'
r2 = 'x'
print(replacechar(s, r1, r2))
