def solution(n):
    """
    진법문제는 진법문제로 접근하자.
    """
    answer = ''
    while True:
        k,r = divmod(n,3)
        if r == 0:
            answer = '4' + answer
            n = k - 1
        else:
            answer = str(r) + answer
            n = k
        if n == 0:
            break
    print(answer)
    return answer
    #기존 시간초과 코드
    # answer = ['1']
    # for i in range(1,n):
    #     idx = -1
    #     while True:
    #         if answer[idx] == '1':
    #             answer[idx] = '2'
    #             break
    #         elif answer[idx] == '2':
    #             answer[idx] = '4'
    #             break
    #         elif answer[idx] == '4':
    #             answer[idx] = '1'
    #             if len(answer) <= abs(idx):
    #                 answer.insert(idx-1,'1')
    #                 break
    #             else:
    #                 idx -= 1
    # print(''.join(answer))
    # return ''.join(answer)