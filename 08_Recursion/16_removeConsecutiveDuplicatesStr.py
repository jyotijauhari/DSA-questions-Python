'''
ip - caabbccdda
op - cabcda
'''

def removeduplicates(str):
    if len(str) == 0 or len(str) == 1:
        return str
    if str[0] == str[1]:
        smalloutput = removeduplicates(str[2:])
        return str[0] + smalloutput
    else:
        smalloutput = removeduplicates(str[1:])
        return str[0] + smalloutput

print(removeduplicates("caabbccdda"))