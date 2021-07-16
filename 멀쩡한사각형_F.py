def solution(w,h):
    totalNum = w * h
    longLine = max(w,h)
    shortLine = min(w,h)
    diff = longLine - 1
    answer = totalNum - (diff // shortLine + 1) * shortLine
    print(answer)
    return answer