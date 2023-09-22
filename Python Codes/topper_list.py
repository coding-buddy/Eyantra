# cook your dish here
names = []
scores = []
topper_list = []
T = int(input())
for case in range(T):
    n = int(input())
    for i in range(n):
        name, score = input().split()
        names.append(name)
        scores.append(float(score))
    max_marks = max(scores)
    count = scores.count(max_marks)
    for j in range(count):
        index = scores.index(max_marks)
        name = names[index]
        topper_list.append(name)
        names.pop(index)
        scores.pop(index)

    topper_list.sort()
    for k in topper_list:
        print(k)