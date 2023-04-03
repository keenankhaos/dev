def find_it(seq):
    seq.sort()
    g=0
    for x in range(len(seq)-1):
        if seq[x]==seq[x+1]:
            seq[x]=seq[x+1]=0
    return sum(seq)        
    


print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))
print(find_it([10]))