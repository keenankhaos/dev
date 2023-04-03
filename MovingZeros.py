def move_zeros(lst):
    c = 0
    nls = []
    for x in lst:
        print(x)
        if x == 0:
            c+=1
        else:
            nls.append(x)
    for x in range(c):
        nls.append(0)
    return nls

print(move_zeros([4,5,2,0,4,2,5,0,0,5]))

