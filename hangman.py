import random
score = 10
true_chars = []
word =["android","bag","tree","install","delete"]
words = random.choice(word)

while True:
    
    for i in range(len(words)):
        if words[i] in true_chars:
            print(words[i],end = '')
        else:
            print('-', end=' ')
    char = input(' \n pleas enter a charcter:')

    if char in words:
        true_chars.append(char)
    else:
        score -=1
    print(score)

    

    if score == 0:
        print("game over")
        break
