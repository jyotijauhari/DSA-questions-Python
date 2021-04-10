#ip - 2,5
#op - 32

def pow(num,power):
    if power == 0:
        return 1
    return num*pow(num, power-1)

print(pow(2,5))