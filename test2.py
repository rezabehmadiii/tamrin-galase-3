a = [2,3,5,10,14]

for i in range(1,len(a)):
    if a[i] < a [i-1]:
        print("no!!!!")
        exit()
else:
        print("yes")