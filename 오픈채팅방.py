def solution(record):
    answer = []
    uidDict = {}
    for i in record:
        uid = i.split(" ")[1]
        action = i.split(" ")[0]
        if action == "Enter":
            uidDict[uid] = i.split(" ")[2]
            answer.append(uid+"님이 들어왔습니다.")
        elif action == "Leave":
            answer.append(uid + "님이 나갔습니다.")
        elif action == "Change":
            uidDict[uid] = i.split(" ")[2]
    for idx,j in enumerate(answer):
        uid = j.split("님이")[0]
        name = uidDict[uid]
        answer[idx] = j.replace(uid, name)
    return answer

    # for i in record:
    #     uid = i.split(" ")[1]
    #     action = i.split(" ")[0]
    #     if len(i.split(" ")) == 3:
    #         uidDict[i.split(" ")[1]] = i.split(" ")[2]
    #         name = i.split(" ")[2]
    #     else:
    #         name = uidDict[i.split(" ")[1]]
    #
    #     if action == 'Enter':
    #         for j in answerDict:
    #             originName = answerDict[j][1].split("님")[0]
    #             tempString = answerDict[j][1].replace(originName, name)
    #             if answerDict[j][0] == uid:
    #                 answerDict[j] = [answerDict[j][0], tempString]
    #         else:
    #             tempString = name + "님이 들어왔습니다."
    #             answerDict[answerNum] = [uid, tempString]
    #             answerNum += 1
    #     elif action == 'Leave':
    #         tempString = name + "님이 나갔습니다."
    #         answerDict[answerNum] = [uid, tempString]
    #         answerNum += 1
    #     elif action == 'Change':
    #         for j in answerDict:
    #             if answerDict[j][0] == uid:
    #                 originName = answerDict[j][1].split("님")[0]
    #                 tempString = answerDict[j][1].replace(originName, name)
    #                 answerDict[j] = [answerDict[j][0], tempString]
    # for i in answerDict:
    #     answer.append(answerDict[i][1])
    #
    # return answer