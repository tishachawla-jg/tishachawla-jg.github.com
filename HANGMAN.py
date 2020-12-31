import random
words=["python","program"]
picked=random.choice(words)
print("The word has",len(picked),"letters")
right=['_']*len(picked)
wrong=[]
c=0
def update():
    for i in right:
        print(i,end="")
    print()
update()
def parts(x):
    if x==0:
        print(' ','----------')
        print(' ','|         |')
        print(' ','|          ')
        print(' ','|          ')
        print(' ','|          ')
        print(' ','|          ')
        print(' ','-----------')
    if x==1:
        print(' ','-----------')
        print(' ','|         |')
        print(' ','|         O')
        print(' ','|          ')
        print(' ','|          ')
        print(' ','|         ')
        print(' ','-----------')
    if x==2:
        print(' ','-----------')
        print(' ','|         |')
        print(' ','|         O')
        print(' ','|         |')
        print(' ','|          ')
        print(' ','|          ')
        print(' ','-----------')
    if x==3:
        print(' ','-----------')
        print(' ','|         |')
        print(' ','|         O')
        print(' ','|         |')
        print(' ','|        -|-')
        print(' ','|         |')
        print(' ','-----------')
    if x==4:
        print(' ','-----------')
        print(' ','|         |')
        print(' ','|         O')
        print(' ','|         |')
        print(' ','|       --|--')
        print(' ','|         |')
        print(' ','-----------')
    if x>=5:
        print(' ','-----------')
        print(' ','|         |')
        print(' ','|         O')
        print(' ','|         |')
        print(' ','|        -|-')
        print(' ','|         |')
        print(' ','|      -- |--')
        print(' ','-----------')
        
while True:
    print("====================")
    guess=input("Guess a letter:")
    if guess in picked:
        index=0
        for i in picked:
            if i==guess:
                right[index]=guess
            index=index+1
        update()
    else:
        if guess not in wrong:
            wrong.append(guess)
        else:
            print('YOU GUESSED THAT')
    if len(wrong)>4:
        print("You lose")
        print("I picked",picked)
        break
    if '_' not in right:
        print("You win")
        break
    parts(c)
    c=c+1
print("BY:/nTISHA CHAWLA")
    

        
        