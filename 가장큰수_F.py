'''

'''

def solution(numbers):
    strAry = []
    for i in numbers:
        i = list(str(i))
        strAry.append(i)
    print(strAry)
    strAry.sort(key=lambda x: (x[0]),reverse=True)

    answer = 9
    return answer