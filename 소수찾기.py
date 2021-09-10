import itertools


def isOdd(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    checkAry = []

    for k in range(1,len(numbers)+1):
        tempNumbers = list(itertools.permutations(numbers,k))
        for i in tempNumbers:
            tempStr = ''
            # 숫자 문자열 생성
            if len(i) == 1:
                tempStr = i[0]
                if tempStr == '0':
                    continue
            else:
                for j in i:
                    tempStr += str(j[0])
            # 적합한 숫자 및 소수인지 판별
            if tempStr[0] == '0':
                continue
            if tempStr != '1' and isOdd(int(tempStr)) and tempStr not in checkAry:
                checkAry.append(tempStr)
                answer += 1

    return answer

