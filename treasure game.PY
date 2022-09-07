print("Welcom to a treasure game.")
choice1 = input('you are at a road. wher do you want to go?"left" or "right".write here \n').lower()
if choice1 == "left":
  choice2 = input('what do you want to do? "swim" or "wait" in the river.\n' ).lower() 
  if choice2 == "wait":
    choice3 = input('in which room do you want to go ? "red" , "blue" or "yellow" \n').lower()
    if choice3 == "red":
     print("your are in the rong room. Game over")
    elif choice3 == "blue":
     print("there is a monstor.Game over")
    elif choice3 == "yellow" :
       print("there is a treasure. You win the game")
    else :
         print("youe have choosed the room which does not exist")
  else: 
      print("there is a deep holein the river.Gamee over")
else:
       print("wrong path so game is over")            

result= input('do you like this game?"yes" or "no" \n')
if result== "yes" : 
  print("Thanks for playing.") 
else:
    print("Better luck for next time.") 