def solution(phone_book):
    '''
    그냥 이중 for문으로 전체를 비교시 효율성이 떨어짐
    비교를 줄일 수 있는 방법이 있을지 고민해보자 sort???
    '''

    answer = True

    for idx, phoneNum in enumerate(phone_book):
        for leftNum in range(idx+1, len(phone_book)):
            if len(phoneNum) > len(phone_book[leftNum]):
                if phoneNum[:len(phone_book[leftNum])] == phone_book[leftNum]:
                    answer = False
                    break
            elif len(phoneNum) < len(phone_book[leftNum]):
                if phone_book[leftNum][:len(phoneNum)] == phoneNum:
                    answer = False
                    break

    return answer