#With list comprehension
list = [i*i for i in range(1,11)] 

'''
#Without list comprehension
list = []
for i in range(1,11):
    list.append(i*i)
'''

print(list)