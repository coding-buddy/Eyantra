from functools import reduce

test_cases = int(input())
for case in range(test_cases):

    names = []
    marks = []

    n = int(input())

    for student in range(n):
        name, score = input().split(" ")
        names.append(name)
        marks.append(score)

    # getting maximum marks
    max = reduce(lambda a,b: a if a>b else b, marks)

    # counting the no. of occurences of max marks
    count = marks.count(max)

    toppers_list = []

    while count>=1:
        toppers_list.append(names[marks.index(max)])
        names.pop(marks.index(max))
        marks.pop(marks.index(max))
        count-=1

    # sorting the list of toppers in ascending alphabetical order
    sorted_list = sorted(toppers_list)

    for i in sorted_list:
        print(i)
