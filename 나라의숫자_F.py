def solution(n):
    """
    21-07-04
    시간 초과를 못잡아 답을 봐버림
    """
    print('123'[2])

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