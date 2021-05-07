"""

       *
      ***
     *****
    *******
     *****
      ***
       *
n = 5
    ..*
    .***
    *****
    .***
    ..*

    ..*
    .***
    *****

    i = n1
    space = n1 - i
    stars = 2*i - 1

n2 =2
i = n2
      .***
      ..*

    i = 1
    space = i
    stars = 2*i - 1

"""

n = 5
n1 = (n+1) // 2
n2 = n1 - 1

i = 1
while(i<=n1):
    space = n1 - i
    print(" "*space, end="")
    stars = 2*i - 1
    print("*"*stars, end="")
    print()
    i += 1

i = n2
while(i>=1):
    space = n2 - i + 1
    print(" "*space, end="")
    stars = 2*i - 1
    print("*"*stars, end="")
    print()
    i -= 1
