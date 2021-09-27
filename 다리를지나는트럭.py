from collections import deque

def solution(bridge_length, weight, truck_weights):

    timetmp = 0
    truck_weights = deque(truck_weights)
    nowTrucks = deque()
    truckInfo = []
    nowWeigth = truck_weights.popleft()     #0초에 한 대 들어감
    truckInfo.append(nowWeigth)
    truckInfo.append(bridge_length)
    nowTrucks.append(truckInfo)

    while True:
        timetmp += 1                            #1초씩 증가

        for idx, i in enumerate(nowTrucks):     #들어온 차들의 남은 거리를 줄여줌
            nowTrucks[idx] = [i[0],i[1]-1]
        if nowTrucks[0][1] == 0:                #맨 앞차의 남은 거리가 0이면 건너는 목록에서 제거
            truckInfo = nowTrucks.popleft()
            tempWeigth = truckInfo[0]
            nowWeigth -= tempWeigth

        if len(truck_weights) == 0:             # 남은 차가 없을 경우
            truckInfo = nowTrucks.pop()
            timetmp += truckInfo[1] + 1       #마지막 차가 남은 거리를 더해줌
            break

        if (nowWeigth + truck_weights[0]) <= weight and (len(nowTrucks) + 1) <= bridge_length:    #차가 들어올 수 있으면 들어옴
            tempWeigth = truck_weights.popleft()
            truckInfo = []
            truckInfo.append(tempWeigth)
            truckInfo.append(bridge_length)
            nowTrucks.append(truckInfo)
            nowWeigth += tempWeigth

    print(timetmp)
    return timetmp