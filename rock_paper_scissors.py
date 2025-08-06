print("===================")
print("Rock Paper Scissors")
print("===================")
player = int(input(" 1)✊\n 2)✋\n 3)✌\n Pick a number: "))
import random
computer = random.randint(1,3)
print(" You chose:      ",player)
print(" Computer chose: ",computer)

if player == 1 and computer == 1:
    print("Tie")
elif player==1 and computer==2:
    print("The computer won!")
elif player==1 and computer==3:
    print("The player won!")
elif player==2 and computer==1:
    print("The player won!")
elif player==2 and computer==2:
    print("Tie")
elif player==2 and computer==3:
    print("The computer won!")
elif player==3 and computer==1:
    print("The computer won!")
elif player==3 and computer==2:
    print("The player won!")
elif player==3 and computer==3:
    print("Tie")
else:
    print("Wrong input")