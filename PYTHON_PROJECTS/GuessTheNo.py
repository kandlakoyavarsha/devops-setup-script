from random import randint
print("Guess The Number Challenge")
name=input("Enter Your Name")
num=randint(0,101)
count=0
flag=1
lb=num-10
ub=num+10
print(num)
while flag:
    guess=int(input("Guess the num between 0 to 100"))
    count+=1
    if(num==guess):
        print('Congratulations {},You guessed the number within {} times'.format(name,count))
        flag=0
    elif(guess<0 or guess>100):
        print("Out Of Bounds")
    elif(count==1):
        if(guess>lb and guess<ub):
            print("Warm")
        else:
            print("Cold")
    else:
        if(guess<temp and guess>lb and guess<ub ):
            print("Warmer")
        else:
            print("Colder")
    temp=guess
        
    

