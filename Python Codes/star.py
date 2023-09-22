# cook your dish here
T = int(input())
for i in range(T):
    n = int(input())
    for i in range(n):
        for j in range(1, n+1-i):
            if (j%5==0):
                print("#", end='')
            else:
                print("*", end='')
        print()