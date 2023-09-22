# cook your dish here
T = int(input())
for i in range(T):
    n = int(input())
    for j in range(n):
        if (j!=n-1):
            if (j==0):
                print(j+3, end=" ")
            elif (j%2==0):
                print(j*2, end=" ")
            else:
                print(j*j, end=" ")
        else:
            if (j==0):
                print(j+3)
            elif (j%2==0):
                print(j*2)
            else:
                print(j*j)