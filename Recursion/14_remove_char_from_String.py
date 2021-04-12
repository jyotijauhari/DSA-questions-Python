'''
ip
string = 'abcabc'
remove = a

op - bcbc
'''

def removeChar(s, r1):
    if len(s) == 0:
        return s

    smallOutput = removeChar(s[1:], r1)
    if s[0] == r1:
        return smallOutput
    else:
        return s[0] + smallOutput

s = 'abcabc'
r1 = 'a'
print(removeChar(s,r1))