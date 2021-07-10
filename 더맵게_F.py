import heapq

def solution(scoville, K):
    """
    heap 자료구조 사용문제.
    최소값을 찾아낼 때 빠름
    """
    count = 0
    heapq.heapify(scoville)
    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            return count
        elif len(scoville) >= 1:
            second = heapq.heappop(scoville)
            newK = first + (second * 2)
            heapq.heappush(scoville, newK)
            count += 1
        elif len(scoville) < 1:
            return -1