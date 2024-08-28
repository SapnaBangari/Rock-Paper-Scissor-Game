""""
workflow of project:
1. Input from user (Rock,paper,scissor)
2. Computer choice(Computer will choose randomly not condotionally)
3. Result print

Cases : 
A - Rock
Rock - Rock = tie
Rock- Paper = Paper win
Rock - scissor = Rock win

B - Paper
Paper - Paper = tie
Paper- Rock = Paper win
Paper - scissor = scissor win

C - Scissor
Scissor - Scissor = tie
Scissor- Rock = Rock win
Paper - scissor = scissor win

"""
game_console='''
 _____________________________   
/        _____________        \  
| == .  |             |     o |  
|   _   |             |    B  |  
|  / \  |             | A   O |  
| | O | |             |  O    |  
|  \_/  |             |       |  
|       |             | . . . |  
|  :::  |             | . . . |  
|  :::  |_____________| . . . |  
|           S N K             |  
\_____________________________/'''
print(game_console)
import random
item_list=["Rock","Paper","Scissor"]
user_choice = input("Enter your move = Rock , Paper , Scissor = ")


comp_choice = random.choice(item_list)

print (f"user_choice = {user_choice} , Computer choice ={ comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same : = Match tie")
    
elif user_choice == "Rock":
    if comp_choice == "Paper":
         print("Paper covers Rock = Computer Win")   
    else:
     print("Rock Smashes Scissor = You Win") 
    
elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts the Paper = Computer Win")       
    else:
      print("Paper covers Rock = You Win")
    
elif user_choice == "Scissor":
    if comp_choice == "Rock":
     print("Rock Smashes Scissor = Computer Win")
    
    else:
     print("Scissor cuts the paper = You Win")
    
    
    