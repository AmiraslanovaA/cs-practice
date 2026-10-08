def winner(names,scores):
    maxind = 0
    max = -100000000000
    for i in range(len(scores)):
        if scores[i] > max:
            maxind = i
            max = scores[i]
    return names[maxind]
def average(scores):
    if scores == []:
        return 0.0
    else:
        sum = 0
        for i in range(len(scores)):
            sum += scores[i]
        return round(sum/len(scores),2)
def ranking(names,scores):
    lst = []
    sortscores = sorted(scores,reverse=True)
    for i in range(len(sortscores)):
        for j in range(len(sortscores)):
            if (sortscores[i] == scores[j]) and (names[j] not in lst):
                lst.append(names[j])
    return lst
def above_average(names,scores):
    lst = []
    for i in range(len(scores)):
        if scores[i] > average(scores):
            lst.append(names[i])
    return lst
