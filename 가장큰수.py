import itertools

def solution(numbers):
    answer = 0
    factorial = list(itertools.permutations((numbers), len(numbers)))
    print(len(factorial))

    for i in factorial:
        temp = ''
        for j in i:
            temp += str(j)
        if int(temp) > answer:
            answer = int(temp)
        print(answer)
    return str(answer)