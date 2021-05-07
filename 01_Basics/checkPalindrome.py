'''
1221
true
'''

def checkPalindrome(n):
    n1 = n
    newnum = 0
    while(n1>0):
        temp = n1%10
        newnum = newnum*10 + temp
        n1 = n1//10
    if newnum == n:
        print("Is Palindrome")
    else:
        print("Not Palindrome")

checkPalindrome(121231)