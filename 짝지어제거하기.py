def solution(s):
    """
    pop 활용 문제
    """
    stack = []
    for i in s:
        stack.append(i)
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    return 1 if len(stack) == 0 else 0

    #기존 시간 초과 코드
    # s = list(s)
    # tempIdx = 1
    # while True:
    #     tempLen = len(s)
    #     for i in range(tempIdx, len(s)):
    #         if s[i-1] == s[i]:
    #             s = s[:i-1] + s[i+1:]
    #             print(tempIdx)
    #             tempIdx = i
    #             break
    #     if tempLen == len(s) or len(s) == 0:
    #         break
    # print(1 if len(s) == 0 else 0)
    # return 1 if len(s) == 0 else 0