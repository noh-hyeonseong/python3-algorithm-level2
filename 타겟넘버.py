answer = 0
tempNumbers = []
tempTarget = 0

def solution(numbers, target):

    global tempNumbers
    tempNumbers = numbers
    global tempTarget
    tempTarget = target

    recurv(numbers[0], 0)
    recurv(-numbers[0], 0)
    print(answer)
    return answer

def recurv(sum, depth):
    if depth == len(tempNumbers) - 1:
        if sum == tempTarget:
            global answer
            answer += 1
            return
        return
    recurv(sum + tempNumbers[depth+1], depth+1)
    recurv(sum - tempNumbers[depth+1], depth+1)
    return


