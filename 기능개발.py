import math

def solution(progresses, speeds):

    answer = []
    end_day = []

    for i, j in zip(progresses, speeds):
        end_day.append(math.ceil((100-i)/j))

    temp = end_day[0]
    for idx, i in enumerate(end_day):
        if idx > 0 and temp >= i:
            answer[-1] += 1
        elif idx > 0 and temp < i:
            answer.append(1)
            temp = i
        elif idx == 0:
            answer.append(1)
            temp = i

    return answer