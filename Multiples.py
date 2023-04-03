number = int(input("Number: "))

def solution(number):
    if number < 0:
        return 0
    else:
        s=0
        for x in range(number):
            if x%3==0 or x%5==0:
                s+=x
        return s

print(solution(number))