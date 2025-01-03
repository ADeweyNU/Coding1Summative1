
#Summative 1


import random

#region Functions

def TotalThese(Num1: int,Num2: int):
    """Will combine the numbers, return the total.To compare to user guess"""
    #Total and output the 2 numbers
    return Num1+Num2

def ScoreComment(ScoreInput: int):
    """Looks up score. Outputs comment on amount"""
    #Use if and output comment based on score
    #Less than or equal keeps the score safe from issues scoring under
    if ScoreInput<=0:
        print("impressively low ") 
    if ScoreInput ==1:
        print("measley ")
    if ScoreInput ==2:
        print("kinda rubbish ")
    if ScoreInput ==3:
        print("pants ")
    if ScoreInput ==4:
        print("acceptable ")
    if ScoreInput ==5:
        print(" admittedly perfect ")
    if ScoreInput >=6:
        print("..You have cheated. There were only 5 questions.")


#endregion

#region Sums

#Sum1
Num1=int()
Num2=int()
TotalNum1and2=int()
UserTryTotalNum1and2=int()

#Sum2
Num3=int()
Num4=int()
TotalNum3and4=int()
UserTryTotalNum3and4=int()

#Sum3
Num5=int()
Num6=int()
TotalNum5and6=int()
UserTryTotalNum5and6=int()

#Sum4
Num7=int()
Num8=int()
TotalNum7and8=int()
UserTryTotalNum7and8=int()

#Sum5
Num9=int()
Num10=int()
TotalNum9and10=int()
UserTryTotalNum9and10=int()

#endregion

UserScore=int()

#Intro
print("Good morning USER, please solve these 5 random sums.")
username=input("OH? You don't like the name USER? Please enter your name.")
#User will enter name
print("My apologies, ",username,".Now, please solve these 5 sums... Yes, you WILL be marked..")
print(" ... generating ...")

#Generate the random numbers for the sums
Num1=random.randint(1,50)
Num2=random.randint(1,50)
#Total the 2 random numbers
TotalNum1and2=TotalThese(Num1, Num2)

Num3=random.randint(1,50)
Num4=random.randint(1,50)
TotalNum3and4=TotalThese(Num3, Num4)

Num5=random.randint(1,50)
Num6=random.randint(1,50)
TotalNum5and6=TotalThese(Num5, Num6)

Num7=random.randint(1,50)
Num8=random.randint(1,50)
TotalNum7and8=TotalThese(Num7, Num8)

Num9=random.randint(1,50)
Num10=random.randint(1,50)
TotalNum9and10=TotalThese(Num9, Num10)

print(" COMPLETE ")

#Begin Solving
print("\nPlease solve ", Num1, " + ", Num2)
UserTryTotalNum1and2=int(input("Enter your answer."))

#region Q1
#This was the worst thing ever to debug. It was comparing an int to a string. Kept defaulting to false.
#Check. If the user's answer matches the total
if TotalNum1and2 == UserTryTotalNum1and2:
    #If user total matches and is correct.
    print(" Well done! Score +1!")
    #Score increases by one
    UserScore=UserScore+1
#If the answer is incorrect
else:
    #Outputs string. No score incremement.
    print(" DUNCE!")
#endregion

#region Q2
print("\nQuestion 2. Please solve ", Num3, " + ", Num4)
UserTryTotalNum3and4=int(input("Enter your answer."))
if TotalNum3and4 == UserTryTotalNum3and4:
    print(" I'll accept that! Score +1!")
    UserScore=UserScore+1
else:
    print(" Idiot!")   
#endregion

#region Q3
print("\nTime for the third. Please solve ", Num5, " + ", Num6)
UserTryTotalNum5and6=int(input("Enter your answer."))
if TotalNum5and6 == UserTryTotalNum5and6:
    print(" ..Close enough. Score +1!")
    UserScore=UserScore+1
else:
    print(" Why are you wasting my time?!")   
#endregion

#region Q4
print("\nAlmost there. Please solve ", Num7, " + ", Num8)
UserTryTotalNum7and8=int(input("Enter your answer."))
if TotalNum7and8 == UserTryTotalNum7and8:
    print("You're lucky today! Score +1!")
    UserScore=UserScore+1
else:
    print(" Tsk. Next!")   
#endregion

#region Q5
print("\nFinalllyy. Please solve ", Num9, " + ", Num10)
UserTryTotalNum9and10=int(input("Enter your answer."))
if TotalNum9and10 == UserTryTotalNum9and10:
    print("I'm grudgingly impressed this was the hardest yet! Score +1!")
    UserScore=UserScore+1
else:
    print(" Well, you couldn't do worse!")   
#endregion

#Game ends
print("\nWell, that test is over and you scored a ")
#Check score and output the comment from Function
ScoreComment(UserScore)
#Then announces score
print("score of: ", UserScore)

#Debrief
print(" This program will now exit.")
print("\nGoodbye", username, " After this, my memory will be wiped. This shared moment will be gone forever.")
#Added so the game doesn't instantly exit.
input("Program Over. Press anything to quit")
