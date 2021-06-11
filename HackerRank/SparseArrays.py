# n*q time, n space
# using dictionary we can solve this in (n+q) time

def count(query, strings):
    count = 0
    for i in strings:
        if i == query:
            count += 1
    return count


def matchingStrings(strings, queries):
    result = []

    for query in queries:
        temp = count(query, strings)
        result.append(temp)

    return result
