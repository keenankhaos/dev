def array_diff(a, b):
    for x in range(len(b)):
        if b[x] in a:
            a = pop(a,b[x])
    return a


def pop(a,n):
    k=[i for i in a if i!=n]
    return k

print(array_diff([1,2,2,2,3],[2]))