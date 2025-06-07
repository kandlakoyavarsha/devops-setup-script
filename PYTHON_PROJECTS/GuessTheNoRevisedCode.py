from random import randint
print(" Welcome to the Guess The Number Challenge!")

print("""
Instructions:
 I have selected a random number between 1 and 100.
 Your task is to guess the number in as few tries as possible.

Rules:
* If your guess is outside the range (1–100), I’ll say "OUT OF BOUNDS".
* On your first guess:
   - If you're within 10 of the number, I’ll say "WARM!"
   - If you're more than 10 away, I’ll say "COLD!"
 * On later guesses:
   - If you're getting closer, I’ll say "WARMER!"
   - If you're moving away, I’ll say "COLDER!"
  Try to guess it in the fewest attempts. Good luck!
""")
name=input("Enter Your Name")
num=randint(1,100)
guesses=[]
while True:
    guess=int(input("Guess the num between 0 to 100"))
    
    if(guess<0 or guess>100):
        print("Out Of Bounds")
        continue
    guesses.append(guess)
    if(num==guess):
        print('Congratulations {},You guessed the number within {} times'.format(name,len(guesses)))
        break
    if(len(guesses)==1):
        if(abs(num-guess)<=10):
            print("WARM!!")
        else:
            print("Cold!!")
    else:
        if(abs(num-guess)<abs(num-guesses[-2])):
            print("WARMER")
        else:
            print("COLDER")