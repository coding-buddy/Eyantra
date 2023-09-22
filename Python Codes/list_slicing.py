# cook your dish here
T = int(input())
for i in range(T):
    n = int(input())
    li = list(map(int, input().split(' ')))
    rev = li[::-1]
    for p in rev:
        print(p, end=' ')
    print()
    for j in range(1, n):
        if (j%3==0):
            print(li[j]+3, end=' ')
    print()
    for j in range(1, n):
        if (j%5==0):
            print(li[j]-7, end=' ')
    print()
    sum = 0
    for k in range(3, 8):
        sum+=li[k]
    print(sum)