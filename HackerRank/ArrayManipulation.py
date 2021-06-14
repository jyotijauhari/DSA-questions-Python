# hint - https://www.youtube.com/watch?v=JtJKn_c9lB4

def arrayManipulation(n, queries):
    
    arr = [0]*(n+1)
    
    for a,b,k in queries:
        arr[a-1] += k
        arr[b] -= k
    
    temp = arr[0]
    maximum = -10
    for i in range(1,len(arr)):
        temp += arr[i]
        maximum = max(maximum, temp)
        
    return maximum
  
#   or

# def arrayManipulation(n, queries):
    
#     arr = [0]*(n+2)
    
#     for a,b,k in queries:
#         arr[a] += k
#         arr[b+1] -= k
    
#     temp = 0
#     maximum = -10
#     for i in arr:
#         temp += i
#         maximum = max(maximum, temp)
        
#     return maximum
