# cook your dish here
T = int(input())
for i in range(T):
    string = input().split()
    length = []
    for j in range(len(string)):
        if (j==0):
            length.append(str(len(string[j])-1))
        else:
            length.append(str(len(string[j])))
    
    print(",".join(length))