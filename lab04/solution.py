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
##def ranking(names,scores):


def above_average(names,scores):
    lst = []
    for i in range(len(scores)):
        if scores[i] > average(scores):
            lst.append(names[i])
    return lst


names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]
print(winner(names,scores))
print(average(scores))
##ranking(names: list[str], scores: list[float]) -> list[str]
print(above_average(names,scores))
