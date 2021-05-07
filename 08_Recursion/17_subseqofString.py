def subs(s):
    if len(s) == 0:
        output =[]
        output.append(" ")
        return output
    smallString = s[1:]
    smalloutput = subs(smallString)

    output = []

    for sub in smalloutput:
        output.append(sub)

    for sub in smalloutput:
        sub_with_zeroth_char = s[0] + sub
        output.append(sub_with_zeroth_char)
    return output

print(subs("abc"))