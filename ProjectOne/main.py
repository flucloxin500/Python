'''بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيم'''
import random

def machine_turn():
    return random.choice([1, -1, 0])  

MeDict = {"Rock": 1, "Paper": -1, "Scissor": 0}
MeDict_Reverse = {1: "Rock", -1: "Paper", 0: "Scissor"}

MeStr = input("Enter your choice (Rock/Paper/Scissor): ")


if MeStr not in MeDict:
    print("Invalid choice! Please enter Rock, Paper, or Scissor.")
else:
    Me = MeDict[MeStr]
    Comp_Turn = machine_turn()

    print(f"Computer chose: {MeDict_Reverse[Comp_Turn]}")

    if Comp_Turn == Me:
        print("It's a tie!")
    elif (Comp_Turn == 1 and Me == -1) or (Comp_Turn == -1 and Me == 0) or (Comp_Turn == 0 and Me == 1):
        print("You Win!")
    else:
        print("You Lose!")
