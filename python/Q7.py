n = list(input("Enter a String: "))
l = len(n)
list = []
for i in range(l):
    j = l-i-1
    list.append(n[j])
if n == list:
    print("Palindrome")
else:
    print("Not Palindrome")