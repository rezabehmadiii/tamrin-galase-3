import random
n = int(input())
a = []
while len(a) < n:
# for i in range(n):
    x = random.randint(0 , 20)
    if x not in a:
        a.append(x)
print(a)






