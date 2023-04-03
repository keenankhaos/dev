def generate_hashtag(s):
    if s == "":
        return False
    else:
        x = s.lower().split()
        gen = "#"
        for y in range(len(x)):
            gen+=x[y][0].upper()
            if len(x[y])>1:
                gen+=x[y][1:len(x[y]):]
        if len(gen)>140:
            return False
        else:
            return gen




print(generate_hashtag('code wars is cool VERY a   VERY'))