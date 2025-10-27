n = int(input())
a = 0
b = 1
c = 0
for i in range(n):
    c = a
    print(a,end=" ")
    a = b           #a,b = b, c+b
    b = c + b