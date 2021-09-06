# FIBONACCI TRAINGLE

'''

n = 5
1 
1 2 
3 5 8 
13 21 34 55 
89 144 233 377 610

cnt1 = 0 
cnt2 = 1 
i = n
j <= i 
print total
cnt1 = cnt2
cnt2 = total

'''
cnt1 = 0 
cnt2 = 1 
n = 4
i = 0 
total = 0 
print(1)
while(i<n):
    j = 0 
    while j<=i+1:
        total = cnt1 + cnt2
        print(total, end = " ")
        cnt1 = cnt2
        cnt2 = total
        j += 1 
    print()
    i += 1 

