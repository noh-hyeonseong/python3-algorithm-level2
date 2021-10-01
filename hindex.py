def solution(citations):
    citations.sort(reverse=True)
    answer = len(citations)
    for idx, i in enumerate(citations):
        if i <= idx:
            return idx
            break
    return answer