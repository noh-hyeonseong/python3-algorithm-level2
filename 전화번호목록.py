def solution(phone_book):
    '''
    그냥 이중 for문으로 전체를 비교시 효율성이 떨어짐
    비교를 줄일 수 있는 방법이 있을지 고민해보자 sort???
    '''

    answer = True
    phone_book.sort()
    for idx, phoneNum in enumerate(phone_book):
        if idx < len(phone_book)-1 and len(phoneNum) < len(phone_book[idx+1]):
            if phoneNum == phone_book[idx+1][:len(phoneNum)]:
                answer = False

    return answer