"""
You are given an array A of size N.  Initially all the elements of the array are zero.

Also, you have an infinite length array S which holds the property that the index is equal to the value of the array i.e for each i (i>=1), S[i] = i.

Now, you have Q queries to perform on array A. Each query contains two variables L and R.

For each query you have to perform the following operation :

For all index i, where L<=i<=R you have to add the value of the array S from the starting position incrementing its positions to the array element at index i, i.e

initialize j = 1

for each i = L to R :

A[i] =A[i] + S[j]

            j = j+1

After performing Q queries, you need to output the final values present in array A.

Input Format
First-line contains an integer N indicating the size of the array indexed from 1 to N.

Second-line contains an integer Q denoting the number of Queries.

It is followed by a Q number of lines where each line contains two space-separated integers L and R.

1 <= N <= 100000
1 <= Q <= 100000
1 <= L <= R <= N
Output Format
Please output the final values present in array A in a space-separated order.



Sample Testcase #0
Testcase Input
5
2 
1 3 
2 4 
Testcase Output
1 3 5 3 0
Explanation
After the first query array becomes

1 2 3 0 0

After second query the array becomes

1 3 5 3 0
"""



def do_operation(arr, l, r):
    j = 1
    
    for i in range(l-1, r):
        arr[i] = arr[i] + j
        j += 1

n = int(input())
arr = [0]*(n)
q = int(input())

for i in range(q):
    l,r = list(map(int,input().strip().split(' ')))
    do_operation(arr, l, r)
    
arr = [str(i) for i in arr]
print(" ".join(arr))
