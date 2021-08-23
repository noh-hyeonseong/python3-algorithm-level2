def solution(s):
    answer = 0
    tempPatern = ""
    paternDick = {}
    tempStr = ""
    min = 1000
    if len(s) == 1:  # 문자열 길이가 1이면 결과는 무조건 1
        return 1
    for i in range(1, int((len(s)+1)/2)+1):       # 몇개로나눌지
        tempStr = ""
        for j in range(0, len(s), i):
            if j == 0:
                tempPatern = s[j:j+i]
                paternDick[s[j:j+i]] = 1
            else:
                if tempPatern == s[j:j+i]:
                    paternDick[s[j:j+i]] += 1
                else:
                    if paternDick[tempPatern] > 1:
                        tempStr = tempStr + str(paternDick[tempPatern]) + tempPatern
                    elif paternDick[tempPatern] == 1:
                        tempStr = tempStr + tempPatern
                    tempPatern = s[j:j+i]
                    paternDick[tempPatern] = 1
            if j + i >= len(s):
                if paternDick[tempPatern] > 1:
                    tempStr = tempStr + str(paternDick[tempPatern]) + tempPatern
                elif paternDick[tempPatern] == 1:
                    tempStr = tempStr + tempPatern
        # print(str(i) + " : " + tempStr)
        if min > len(tempStr):
            min = len(tempStr)
    answer = min
    # print(answer)
    return answer