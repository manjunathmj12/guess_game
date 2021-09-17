def level():
    live=3
    time=0
    chance=0
    point1=0
    guess=random.randint(0,5)
    while time<live:
        inputnum=int(input("guess the number:"))
        time+=1
        chance+=1
        if guess == inputnum:
            print("congrats you guessed in ",chance,"th try")
            if chance==1:
                point1=30
            elif chance==2:
                point1=20
            elif chance==3:
                point1=10
            else:
                print("better luck next time")
            print("in this round you have earned \t\t\t\t\t",point1,"points ")

            live=5
            time=0
            chance=0
            point2=0
            guess=random.randint(0,10)
            print("\n \t \t \t  welcome to level 2:")
            while time<live:
                inputnum=int(input("guess the number:"))
                time+=1
                chance+=1
                if guess == inputnum:
                    print("congrats you guessed in ",chance,"th try")
                    if chance==1:
                        point2=50
                    elif chance==2:
                        point2=40
                    elif chance==3:
                        point2=30
                    elif chance==4:
                        point2=20
                    elif chance==5:
                        point2=10
                    else:
                            exit()
                    print("in this round you have earned \t\t\t\t\t",point2,"points ")

                    live=10
                    time=0
                    chance=0
                    point3=0
                    guess=random.randint(0,100)
                    print("\n \t  \t \t welcome to last level :")
                    while time<live:
                        inputnum=int(input("guess the number:"))
                        time+=1
                        chance+=1
                        if guess == inputnum:
                            print("congrats you guessed in ",chance,"th try")
                            if chance<=2:
                                point3=50
                            elif chance<=4:
                                point3=40
                            elif chance<=6:
                                point3=30
                            elif chance<=8:
                                point3=20
                            elif chance<=10:
                                point3=10
                            else:
                                exit()
                            print("in this round you have earned \t\t\t\t\t",point3,"points ")
                            print("you won the game ")
                            points=point1+point2+point3
                            print("congralutions you earned ",points,"in total")
                            if points>100:
                                print("\t \t \t you won a maclaptop")
                            elif points>70:
                                print("\t \t \t you won a iphone")
                            elif points>50:
                                print("\t \t \t you won a bicycle")
                        elif guess > inputnum:
                            print("you guessed small ")
                        elif guess < inputnum:
                            print("you guessed big ")
                        else:
                            exit()

                elif guess > inputnum:
                    print("you guessed small ")
                elif guess < inputnum:
                    print("you guessed big")
                else:
                    exit()

        elif guess > inputnum:
            print("you guessed small ")
        elif guess < inputnum:
            print("you guessed big")
        else:
            exit()






def manual():
    lower=int(input("type the lower limit:"))
    upper=int(input("type the upper limit:"))
    live=round(math.log(upper - lower + 1, 2))
    print("you have ",live,"chances to guess the number")
    time=0
    chance=0
    guess=random.randint(lower,upper)
    while time<live:
        inputnum=int(input("\ntype the number:"))
        time+=1
        chance+=1
        if guess == inputnum:
            print("congrats you guessed in ",chance,"th try")
            print("\n\t\t\tyou won the game")
            exit()
        elif guess > inputnum:

            print("you guessed small ")
        elif guess < inputnum:
            print("you guessed big")
        else:
            print("better luck next time")


##def timer():
##    mintt = 15
##    timer = int(mintt)
##    while(timer !=0):
##        live=mintt
##        time=0
##        chance=0
##        point3=0
##        guess=random.randint(0,100)
##        while time<live:
##            inputnum=int(input("\ntype the number:"))
##            time+=1
##            chance+=1
##            if guess == inputnum:
##                print("congrats you guessed in ",chance,"th try")
##                print("\n\t\t\tyou won the game")
##                exit()
##            elif guess > inputnum:
##                print("you guessed small ")
##            elif guess < inputnum:
##                print("you guessed big")
##            else:
##                print("better luck next time")
##        timer=timer-1
##        time.sleep(1)
##        print("\t \t \t \t \t \t \t ",timer)


##def timer():
##    
##    guess=random.randint(0,5)
##    while True:
##        starttime=time()
##        inputnum=int(input("enter the number:"))
##        if inputnum == guess:
##            print("you won")
##            endtime=time()
##            time=(startime - endtime)
##            print(time)
##        if inputnum > guess:
##            print("you guessed small")
##        if inputnum > guess:
##            print("you guessed big")




####################################################################################################################################################################


import random
import math
import time

print("\t \t \t welome to the guess game✌:")
print("do you manual mode or level mode\nfor manual press m for level press l:")
answer=input("enter M or L or T:")
if answer == 'm':
    manual()
elif answer =='l':
    print(" \nthe level are \n level 1 is 0 to 5(3 chances) \n level 2 is 0 to 10(5 chances) \n level 3 is 0 to 100(10 chances):")
    print(" lets begin !!!!\n \t \t \t  all the best ")
    level()
    print("\t \t \t better luck next time")
# elif answer =='t':
#     timer()


########################################################################################################