n = list(input())
c = 0
l = ['A','E','I','O','U','a','e','i','o','u']
for i in n:
    if i in l:
        c = c + 1
print(c)

'''
#shorter one
n = input()
l = 'AEIOUaeiou'
c = sum(1 for ch in n if i in l)
print(c)
'''