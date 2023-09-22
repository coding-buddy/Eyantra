# cook your dish here
# Import reduce module
from functools import reduce


# Function to generate the A.P. series
def generate_AP(a1, d, n):

    AP_series = []

    for i in range(n):
        an = a1 + (i)*d
        AP_series.append(an)

    return AP_series


# Main function
if __name__ == '__main__':
    
    T = int(input())

    for i in range(T):
        a1, d, n = list(map(int, input().split()))
        AP_series = generate_AP(a1, d, n)
        
        sqr_AP_series = [x*x for x in AP_series]

        sum_sqr_AP_series = 0
        for num in sqr_AP_series:
            sum_sqr_AP_series += num
            
        for i in AP_series:
            print(i, end=' ')
        
        for i in sqr_AP_series:
            print(i, end=' ')
        
        print(sum_sqr_AP_series)