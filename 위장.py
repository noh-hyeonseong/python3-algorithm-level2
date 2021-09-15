import itertools

def solution(clothes):
    answer = 0
    dick = {}

    for i in clothes:
        answer += 1
        if i[1] in dick:
            dick[i[1]] += 1
        else:
            dick[i[1]] = 1
    tempAry = []
    for i in dick:
        tempAry.append(dick[i])
    for i in range(2,len(tempAry)+1):
        result = list(itertools.combinations(tempAry,i))
        for j in result:
            tempNum = 1
            for q in j:
                tempNum *= q
            answer += tempNum

    print(answer)
    return answer

