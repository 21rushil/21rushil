import random
choices = ["rock","paper","scissor"]

computer = random.choice(choices)
player = None

while player not in choices:
    player = input("rock , paper , scissor?:").lower()


       if player == computer:
  print("computer: ",computer)
  print("player:" , player)
  print("Tie!")
 elif player == "rock"
   if computer == "paper":
    print("computer: ", computer)
print("player:" , player)
print("You Lose")
if computer == "scissor":
    print("computer: ", computer)
print("player:" , player)
print("You Win")

elif player == "scissor":
  if computer == "rock":
    print("computer: ", computer)
print("player:" , player)
print("You Lose")
if computer == "paper":
    print("computer: ", computer)
print("player:" , player)
print("You Win")


elif player == "paper":
  if computer == "scissor":
    print("computer: ", computer)
print("player:" , player)
print("You Lose")
if computer == "rock":
    print("computer: ", computer)
print("player:" , player)
print("You Win")




