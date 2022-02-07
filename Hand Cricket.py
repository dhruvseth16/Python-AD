import random
list1= [1,2,3,4,6]

total_balls= 36
ball_initial= 0
your_runs= 0
target=0
 
#1st inning
print ("-----------------------------------------------\nYour Batting\n")
while total_balls > ball_initial:
    
    runs= int(input("Enter Runs for Your Batting Turn: "))
    comp_ball= random.choice(list1)

    if runs==comp_ball:
        print ("You scored: ",runs,",Computer Guessed: ",comp_ball)
        print ("You are Out!. Your Total Runs= ", your_runs,"\n")
        break
    elif runs>6 or runs==5:
        print ("OHHnoo..Cmmon! You Cannot Hit More than a six or score a five, BE PRACTICAL LOL!\n")
        continue
    else:
        your_runs= your_runs+runs
        print ("Your Guess: ",runs,",Computer Guess: ",comp_ball)
        print ("Your runs Now are: ",your_runs,"\n")

    ball_initial= ball_initial + 1  

#2nd inning
list2= [1,2,3,4,6]

total_balls_final= 36
ball_final= 0
comp_runs= 0
print ("-----------------------------------------------")
print("target is: ",your_runs+1)
target=your_runs+1
print ("-----------------------------------------------\n\nComputer Batting\n")

while ball_final < total_balls_final :

    ball= int(input("Enter Runs for Your Balling Turn: "))
    comp_bat= random.choice(list2)

    if comp_bat==ball:
        print ("Computer Scored: ",comp_bat,"Your Guess: ",ball)
        print ("The Computer is Out. Computer Runs= ",comp_runs,"\n")
        break

    elif ball>6 or ball==5:
        print ("OHHnoo..Cmmon! You Cannot guess the opponent to score more than a six or a five, BE PRACTICAL LOL\n")
        continue
    
    else:
        comp_runs= comp_runs+comp_bat
        print ("Computer Scored: ",comp_bat,"Your Guess: ",ball)
        print ("Computer Runs: ",comp_runs,"\n")

        if comp_runs >= target:
            break
        
    ball_final = ball_final+1

#Results
print ("\n-----------------------------------------------\nRESULTS: ")

if comp_runs < target:
    print ("\nYou won the Game.\n\nYour Total Runs= ",your_runs,"  \n[Balls Played (Out of 36): ",ball_initial+1,"]","\n\nComputer Total Runs= ",comp_runs,"  \n[Balls Played (Out of 36): ",ball_final+1,"]\n")   

elif comp_runs == your_runs:
    print ("The Game is a Tie")

else:
    print ("\nComputer won the Game.\n\nComputer Total Runs= ",comp_runs,"  \n[Balls Played (Out of 36): ",ball_final+1,"]","\n\nYour Total Runs= ",your_runs,"  \n[Balls PLayed (Out of 36): ",ball_initial+1,"]\n")

