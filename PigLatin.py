def pig_it(text):
    w = text.split()
    for x in range(len(w)):
        if w[x].isalnum():
            w[x]=w[x][1:]+w[x][0]+"ay"
    return " ".join(w)
    


print(pig_it('Pig latin is cool'))