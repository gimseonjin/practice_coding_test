import operator


def getPoint(countOfThree, countOfTwo, countOfOne):
    a = {}
    for i in range(3):
        a[i] = countOfThree[i]*3+countOfTwo[i]*2+countOfOne[i]*1

    print(a)
    a = sorted(a.items(), key=operator.itemgetter(1), reverse=True)
    print(a)

    return a


n = int(input())
votes = []
countOfThree = {0: 0, 1: 0, 2: 0}
countOfTwo = {0: 0, 1: 0, 2: 0}
countOfOne = {0: 0, 1: 0, 2: 0}

for i in range(n):
    a, b, c = map(int, input().split(" "))
    votes.append([a, b, c])

for i in votes:
    for j in range(3):
        if i[j] == 3:
            countOfThree[j] = countOfThree[j]+1
        elif i[j] == 2:
            countOfTwo[j] = countOfTwo[j]+1
        else:
            countOfOne[j] = countOfOne[j]+1

print(countOfThree)
print(countOfTwo)
print(countOfOne)

print(getPoint(countOfThree, countOfTwo, countOfOne))
