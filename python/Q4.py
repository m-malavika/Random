n = int(input())
if n > 0:
    k = n//2 + 1
    flag = 0
    for i in range(2,k):
        if n % i == 0:
            flag = 1
            break
    if flag == 0:
        print("prime")
    else:
        print("Not prime")