def solution(citations):
    citations.sort(reverse=True)
    for idx, i in enumerate(citations):
        answer = idx
        if i <= idx:
            answer = idx
            break
    return answer