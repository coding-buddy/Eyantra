n = int(input())
for i in range(n):
    a = input()
    a = a.lower()
    b = a[::-1]
    if (a==b):
        print("It is a palindrome")
    else:
        print("not a palindrome")