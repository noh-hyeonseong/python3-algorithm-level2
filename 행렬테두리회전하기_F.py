def solution(rows, columns, queries):
    '''
    테스트 케이스 통과
    제출 후 채점에서 통과못함
    '''
    answer = []
    matrix = []
    count = 1
    for i in range(0, rows):
        tempMatrix = []
        for j in range(0, columns):
            tempMatrix.append(count)
            count += 1
        matrix.append(tempMatrix)

    for query in queries:
        tempAry = []
        leftNum = []
        if query[3] == query[1] and query[2] == query[0]:
            answer.append(matrix[query[0]-1][query[1]-1])
        elif query[3] == query[1]:
            for row in range(query[0]-1,query[2]):
                tempAry.append(matrix[row][query[3]-1])
            lastNum = tempAry.pop()
            tempAry.reverse()
            tempAry.append(lastNum)
            answer.append(min(tempAry))
            for row in range(query[0] - 1, query[2]):
                matrix[row][query[3]-1] = tempAry.pop()
        elif query[2] == query[0]:
            for column in range(query[1]-1,query[3]):
                tempAry.append(matrix[query[3]-1][column])
            lastNum = tempAry.pop()
            tempAry.reverse()
            tempAry.append(lastNum)
            answer.append(min(tempAry))
            for column in range(query[1] - 1, query[3]):
                matrix[query[3]-1][column] = tempAry.pop()
        else:
            for column in range(query[3], query[1]-1, -1):
                if column == query[3]:
                    for row in range(query[0], query[2] + 1):
                        tempAry.append(matrix[row - 1][column - 1])
                elif column == query[1]:
                    for row in range(query[2], query[0]-1, -1):
                        tempAry.append(matrix[row - 1][column - 1])
                else:
                    tempAry.append(matrix[query[2] - 1][column-1])
                    leftNum.append(matrix[query[0] - 1][column-1])
            while len(leftNum) > 0:
                tempAry.append(leftNum.pop())

            lastNum = tempAry.pop()
            tempAry.reverse()
            tempAry.append(lastNum)
            answer.append(min(tempAry))
            # print(tempAry)

            for column in range(query[3], query[1]-1, -1):
                if column == query[3]:
                    for row in range(query[0], query[2] + 1):
                        matrix[row - 1][column - 1] = tempAry.pop()
                elif column == query[1]:
                    for row in range(query[2], query[0]-1, -1):
                        matrix[row - 1][column - 1] = tempAry.pop()
                else:
                    matrix[query[2] - 1][column-1] = tempAry.pop()
            # print(tempAry)
            for i in range(query[1]+1, query[3]):
                matrix[query[0]-1][i] = tempAry.pop()
    print(answer)
    return answer