import random
user_rooot= input("Please chose your value(R/P/S) : ")
computer_root=["Rock","Paper","Scissors"]
computer_action = random.choice(computer_root)
if user_rooot=="R":
    if computer_action=="Scissors":
        print(f"Your action is:{user_rooot} , Computer action is :{computer_action} === You win ")
    else :
        print(f"Your action is:{user_rooot} , Computer action is :{computer_action} === You Loss , booo")
elif user_rooot=="P":
    if computer_action=="Rock":
        print(f"Your action is:{user_rooot} , Computer action is :{computer_action} === You win ")
    else :
        print(f"Your action is:{user_rooot} , Computer action is :{computer_action} === You Loss ! booooo ")
elif user_rooot=="S":
    if computer_action =="Paper":
      print(  f"Your action is:{user_rooot} , Computer action is:{computer_action} ===.....You win ..... ")
    else :
        print(f"Your action is:{user_rooot} , Computer action is:{computer_action} === You Loss ! boooo ")
