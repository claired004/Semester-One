#Claire Deng
#1/7/2025
#Rock Paper Scissors

#Init
import random
score = 0 #number of questions answered correctly
questions = 0 #number of questions answered


#function
def quiz():
    global score
    global questions
    print("""Welcome to the Multiplication Quiz!
          You will be given multiplication problems to solve. Good Luck!""")
while True:

    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    answer = int("What is "+str(num1)+" x "+str(num2)+"?")
    print("You got "+str(score)+"/"+str(questions)+" questions correct!")
    print(str(num1)+" x "+str(num2)+" = "+str(num1*num2))
    print("You answer: "+str(answer))
    if int(answer)==int(num1*num2):
        score=score+1
        print("You got that CORRECT!")
    else:
        print("Sorry, that was INCORRECT!")
    questions=questions+1


#main
quiz()
