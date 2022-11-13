

 
#starting

import random
list1= [1,2,3,4,6]

total_balls= 0
ball_initial= 0
your_runs= 0
target=0

list2= [1,2,3,4,6]
total_balls_final= 0
ball_final= 0
comp_runs= 0
#choice of innings

inst = "WELCOME TO THE GAME OF HAND CRICKET\n"
print(inst.center(144, " "))
print("""1. You can select which kind of innings you want to play.
2. You will then have to pick a side for the toss.
3. If you win, you bat first, but if you lose, computer bats first.
4. When batting, you have to input runs and while balling you have to guess the runs scored by the computer.
5. If your runs match with the computer's guess you are out ! (and vice versa when you ball)\n""")

print("Start (Yes/No) : ")
x = input("")
for i in x:
    if x.upper() == "YES" or x.upper() == "Y":

        while True:
            print(f"Hey !!!\nWhich type of innings u wanna play ?\na. 1 over\nb. 3 overs\nc. 5 overs")
            choice = input("")
            repeat = ''
            if choice.upper()=="A":
                total_balls,total_balls_final=6,6
                print("\nYou have selected for 1 over")
                break
            elif choice.upper()=="B":
                total_balls,=18
                print("\nYou have selected for 3 overs")
                break
            elif choice.upper()=="C":
                total_balls==30
                print("\nYou have selected for 5 overs")
                break
            else: 
                print("\nPlease select any 1 out of the given options")
                print ("-----------------------------------------------\n")

        #Toss
        print(f"\nPick your side?\na. Head\nb. Tail\n")
        choice_toss = input("")
        repeat = ''
            
        list_toss=["You won", "You lost"]

        result=random.choice(list_toss)
        print(result)


        if result=="You won":
        #1st inning
            print ("-----------------------------------------------\n\nYou Bat First...\n")
            while total_balls > ball_initial:
            
                runs= int(input("Enter Runs for Your Bat first: "))
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




            print ("-----------------------------------------------")
            print("target is: ",your_runs+1)
            target=your_runs+1
            print ("-----------------------------------------------\n\nComputer Batting\n")
            
            while ball_final < total_balls_final :

                ball= int(input("guess Runs for comp Balling Turn: "))
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

            #result1
            print ("\n-----------------------------------------------\nRESULTS: ")

            if comp_runs < target:
                print ("\nYou won the Game.\n\nYour Total Runs= " ,your_runs, "\nComputer Total Runs= " ,comp_runs, "\n")   

            elif comp_runs == your_runs:
                print ("The Game is a Tie")

            else:
                print ("\nComputer won the Game.\n\nComputer Total Runs= " ,comp_runs, "\nYour Total Runs= " ,your_runs)

            

        #you lost
        if result=="You lost":
            print ("-----------------------------------------------\n\nComputer Bats First\n")
            
            while total_balls > ball_initial:
            

                ball= int(input("Guess Runs for Your Balling Turn: "))
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

                ball_initial= ball_initial + 1
                    
            print ("Your target is: ",comp_runs+1)
            target=comp_runs+1
            
            #Your lost second inning
            print ("-----------------------------------------------\n\nYour Batting now...\n")
            while total_balls > ball_final:
            
                runs= int(input("Enter Runs for Your Bat first: "))
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

                 
                    if your_runs >= target:
                        break

                    ball_final= ball_final + 1



        #Results_2
                   
            print ("\n-----------------------------------------------\nRESULTS: ")

            if your_runs >= target:
                print ("\nYou won the Game.\n\nYour Total Runs= ",your_runs, "\nComputer Total Runs= ",comp_runs)   

            elif comp_runs == your_runs:
                print ("The Game is a Tie")

            else:
                print ("\nComputer won the Game.\n\nComputer Total Runs= ",comp_runs,"\nYour Total Runs= ",your_runs)
        break

    else:
        if x.upper() == 'NO' or x.upper() == "N":
            print("then why did you run the game in the first place..!!?")
            break
  


