import csv
import random
import time


	
	# using sleep() to halt execution
	


list1= [1,2,3,4,6]
total_balls= 0
ball_initial= 1
your_runs= 0
target=0

list2= [1,2,3,4,6]
total_balls_final= 0
ball_final= 1
comp_runs= 0

#function of rules defined
def rules():

    inst = "WELCOME TO ADCC- Atharva-Dhruv Cricket Champiaonship\n"
    print(inst.center(160, " "))
    print("""    1. You can select which kind of innings you want to play.
    2. You will then have to pick a side for the toss.
    3. If you win, you bat first, but if you lose, computer bats first.
    4. When batting, you have to input runs and while balling you have to guess the runs scored by the computer.
    5. If your runs match with the computer's guess you are out ! (and vice versa when you ball)
    6. Select your team out of the 8 teams with the code in brackets and computer will set a team for itself as your opponent\n
 India(1)\n New Zealand(2)\n Pakistan(3)\n Australia(4)\n England(5)\n South Africa(6)\n Sri Lanka(7)\n Bangladesh(8)\n """)

#team selection game conditions
def team():
    while True:
            print("Select your team out of the above mentioned with its code")
            global your_team
            choice_team = input("")
            repeat = ''
            if choice_team=="1":
                print("\nYour team is India")
                your_team="India"
                break
            if choice_team=="2":
                print("\nYour team is NZ")
                your_team="NZ"
                break
            if choice_team=="3":
                print("\nYour team is PAK")
                your_team="PAK"
                break
            if choice_team=="4":
                print("\nYour team is AUS")
                your_team="AUS"
                break
            if choice_team=="5":
                print("\nYour team is ENG")
                your_team="ENG"
                break
            if choice_team=="6":
                print("\nYour team is SA")
                your_team="SA"
                break
            if choice_team=="7":
                print("\nYour team is SL")
                your_team="SL"
                break
            if choice_team=="8":
                print("\nYour team is BAN")
                your_team="BAN"
                break
            else:
                print("\nPlease select any one out of the given options")
    return your_team
    print ("-----------------------------------------------\n")




#starting
def opponent():
    print(f"\nComputer is selecting an opponent")


    list_opponent=["India", "NZ", "PAK", "AUS", "ENG", "SA", "SL", "BAN"]

    global opponent
    while True:
        opponent=random.choice(list_opponent)

        if opponent==your_team:
            continue
        else:
            break


    print(opponent)
    print ("-----------------------------------------------\n")

    print("The match is", your_team, "vs", opponent)
    print ("-----------------------------------------------\n")
    print("\n")

#selection of overs defined
def selecting_overs():
    while True:
            print(f"Select innings type:\nWhich type of innings u wanna play ?\na. 1 over\nb. 3 overs\nc. 5 overs")
            choice = input("")
            repeat = ''
            if choice.upper()=="A":
                global total_balls,total_balls_final
                total_balls,total_balls_final=6,6
                print("\nYou have selected for 1 over")
                break
            elif choice.upper()=="B":
                total_balls,total_balls_final
                total_balls,total_balls_final=18,18
                print("\nYou have selected for 3 overs")
                break
            elif choice.upper()=="C":
                total_balls,total_balls_final
                total_balls,total_balls_final=30,30
                print("\nYou have selected for 5 overs")
                break
            else:
                print("\nPlease select any 1 out of the given options")
                print ("-----------------------------------------------\n")

#toss function defined
def toss():
    print(f"\nPick your side?\na. Head\nb. Tail\n")
    choice_toss = input("")
    repeat = ''

    list_toss=["You won", "You lost"]

    global result
    result=random.choice(list_toss)
    print(result)



#game function defined
def game(result):
    if result=="You won":
            #1st inning
            print ("-----------------------------------------------\n\n",your_team,"Bats First...\n")
            global ball_initial, your_runs, ball_final, comp_runs
            while total_balls > ball_initial:

                runs= int(input("Enter Runs for Your Batting: "))
                comp_ball= random.choice(list1)

                if runs==comp_ball:
                    print ("You scored: ",runs,",Computer Guessed: ",comp_ball)
                    print ("You are Out!. Your Total Runs= ", your_runs,)
                    print ("Balls played: ",ball_initial,"\n")
                    break
                elif runs>6 or runs==5:
                    print ("OHHnoo..Cmmon! You Cannot Hit More than a six or score a five, BE PRACTICAL LOL!")
                    continue
                else:
                    your_runs= your_runs+runs
                    print ("Your Guess: ",runs,",Computer Guess: ",comp_ball)
                    print ("Your runs Now are: ",your_runs)
                    print ("Balls played: ",ball_initial,"\n")
                ball_initial= ball_initial + 1

            #2nd inning
            print ("-----------------------------------------------")
            print("target is: ",your_runs+1)
            global target
            target=your_runs+1
            print ("-----------------------------------------------\n\n",opponent," Batting\n")

            while ball_final < total_balls_final :

                ball= int(input("Guess Runs for your Balling Turn: "))
                comp_bat= random.choice(list2)

                if comp_bat==ball:
                    print ("Computer Scored: ",comp_bat,"Your Guess: ",ball)
                    print ("The Computer is Out. Computer Runs= ",comp_runs,"\n")
                    print ("Balls played: ",ball_final,"\n")
                    break

                elif ball>6 or ball==5:
                    print ("OHHnoo..Cmmon! You Cannot guess the opponent to score more than a six or a five, BE PRACTICAL LOL\n")
                    continue

                else:
                    comp_runs= comp_runs+comp_bat
                    print ("Computer Scored: ",comp_bat,"Your Guess: ",ball)
                    print ("Computer Runs: ",comp_runs,"\n")
                    print ("Balls played: ",ball_final,"\n")

                    if comp_runs >= target:
                        break

                    ball_final = ball_final+1


    #Toss lost
    if result=="You lost":
        print ("-----------------------------------------------\n\n",opponent,"Bats First\n")
        #1st inning
        while total_balls > ball_initial:

            ball= int(input("Guess Runs for Your Balling Turn: "))
            comp_bat= random.choice(list2)

            if comp_bat==ball:
                print ("Computer Scored: ",comp_bat,"Your Guess: ",ball)
                print ("The Computer is Out. Computer Runs= ",comp_runs,"\n")
                print ("Balls played: ",ball_initial,"\n")
                break

            elif ball>6 or ball==5:
                print ("OHHnoo..Cmmon! You Cannot guess the opponent to score more than a six or a five, BE PRACTICAL LOL\n")
                continue

            else:
                comp_runs= comp_runs+comp_bat
                print ("Computer Scored: ",comp_bat,"Your Guess: ",ball)
                print ("Computer Runs: ",comp_runs,"\n")
                print ("Balls played: ",ball_initial,"\n")

            ball_initial= ball_initial + 1

        print ("Your target is: ",comp_runs+1)
        target=comp_runs+1

        #2nd inning
        print ("-----------------------------------------------\n\nYour Batting now...\n")
        while total_balls > ball_final:

            runs= int(input("Enter Runs for Your Bat first: "))
            comp_ball= random.choice(list1)

            if runs==comp_ball:
                print ("You scored: ",runs,",Computer Guessed: ",comp_ball)
                print ("You are Out!. Your Total Runs= ", your_runs,"\n")
                print ("Balls played: ",ball_final,"\n")
                break
            elif runs>6 or runs==5:
                print ("OHHnoo..Cmmon! You Cannot Hit More than a six or score a five, BE PRACTICAL LOL!\n")
                continue
            else:
                your_runs= your_runs+runs
                print ("Your Guess: ",runs,",Computer Guess: ",comp_ball)
                print ("Your runs Now are: ",your_runs,"\n")
                print ("Balls played: ",ball_final,"\n")


                if your_runs >= target:
                    break

                ball_final= ball_final + 1

#outcome function defined
def outcome(result):
    if result=="You won": #result1
        print ("\n-----------------------------------------------\nRESULTS: ")
        for i in range(3,0,-1):
            time.sleep(1)
            print('.')
        if comp_runs < target:
            print ("\n",your_team," won the Game.\n\n", your_team,"Total Runs= " ,your_runs, "\n",opponent," Total Runs= " ,comp_runs, "\n")
            wonteam = your_team
        elif comp_runs == your_runs:
            print ("The Game is a Tie")
            

        else:
            print ("\n",opponent," won the Game.\n\n",opponent," Total Runs= " ,comp_runs, "\n",your_team,"Total Runs= " ,your_runs)

    elif result=="You lost": #Results_2
        print ("\n-----------------------------------------------\nRESULTS: ")

        if your_runs >= target:
            print ("\n",your_team,"won the Game.\n\nYour Total Runs= ",your_runs, "\nComputer Total Runs= ",comp_runs)

        elif comp_runs == your_runs:
            print ("The Game is a Tie")

        else:
            print ("\n",opponent," won the Game.\n\nComputer Total Runs= ",comp_runs,"\nYour Total Runs= ",your_runs)


'''def filehandling():
    game= open("Stats.csv", 'a')
    stuwriter = csv.writer(game)
    stuwriter.writerow(['Teams','matches','points'])
    if your_team == "India" and :
        stuwriter.writerow(['India','1','2'])
    if your_team == "NZ":
        stuwriter.writerow(['New Zealand','1','2'])
    stuwriter.writerow(['PAK'])
    stuwriter.writerow(['aus'])
    stuwriter.writerow(['ENG'])
    stuwriter.writerow(['SA'])
    game.close()'''



#main code
print("Start (Yes/No) : ")
x = input("")


for i in x:
    if x.upper() == "YES" or x.upper() == "Y":
        '''print ("Starting in: ")
        for i in range(3,-1,-1):
            time.sleep(1)
            print(i)'''
        while True
        rules() #rules called
        team()#team selection called
        opponent()#opponent selection called
        selecting_overs() #selection_overs called
        toss() #toss called
        game(result) #game called
        outcome(result) #outcome called
        #filehandling()


    else:
        if x.upper() == 'NO' or x.upper() == "N":
            print("then why did you run the game in the first place..!!?")
    break


#konsa over kitti ball chal rahi hai ye bhi print hhona chaiye
