import random

nom =input("enter the name")
user_score = 0
pc_score = 0
null = 0

while True:
    user_player = input("enter :(s)tone , (p)aper ,(c)issor , (q)uitter: "  ) 
    if user_player == "q":
           print("you quit the game")
           break
    if user_player != "s" and user_player != "p" and user_player != "c" :
           continue
    if user_player == "s":
           print("stone again ",end =" ")
    elif user_player == "p":
           print("paper again ",end =" ")       
    else :
           print("scissor again ",end =" ")       
    
    user_pc =random.randint(1,3) 
    if user_pc == 1:
           user_pc = "s"
           print("stone")
    elif user_pc == 2:
           user_pc = "p"
           print("paper")      
    else :
           user_pc = "c"
           print("scissor")

    if user_player == user_pc :
           print("it is null")
           null += 1
    elif user_player == "s" and user_pc =="p":
           print("pc win")
           pc_score +=1
    elif user_player == "s" and user_pc =="c":
           print("user_player win")
           user_score +=1
    elif user_player == "p" and user_pc =="s":
           print("player win") 
           user_score +=1
    elif user_player == "p" and user_pc =="c":
           print("pc win")
           pc_score +=1
    elif user_player == "c" and user_pc =="s":
           print("player win")
           user_score +=1
    elif user_player == "c" and user_pc =="p":
           print("player win")
           user_score +=1


