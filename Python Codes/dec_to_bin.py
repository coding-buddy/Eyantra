# cook your dish here
def dec_to_binary(n):

    bin_num = ''

    for i in range(8):
        bit = str(n%2)
        bin_num += bit
        n = n//2
        
    bin_num = bin_num[::-1]
    return bin_num


# Main function
if __name__ == '__main__':
    test_cases = int(input())
    for case in range(1,test_cases+1):
        n = int(input())
        bin_num = dec_to_binary(n)
        print(bin_num)
    