sentence = input("Sentence: ")

def spin_words(sentence):
    w = sentence.split()
    for x in range(len(w)):
        if len(w[x])>4:
            w[x]=w[x][::-1]
    return " ".join(w)


print(spin_words(sentence))
