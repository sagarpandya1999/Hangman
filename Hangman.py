print("welcome to the game named Bollywood-Hollywood")
print("INSTRUCTIONS:")
print("       this is two player game")
print("       you have to enter movie name and some char. for hint to other player")
print("       other player have to enter one by ne char. that he wants to put in string")
print("       if your guess is right comp. fill that string with your char in right position and you have to guess other character")
print("       you have 9 wrong attempt for guess the whole movie name")
print("       if your char. guess is wrong comp. will reduce your remaining attempt and when you cross the limit comp. break the program and turn will be change.")
print("       if you find right ans. within the given limit your rank will be improve by your reamaining attempts")
print("       ")
print("BEST OF LUCK :)")
print(" ")
t=0
Player1Rank = 0
Player2Rank = 0
Turn = 1
NoofRound = int(input("enter no. of round you want to play"))
Player1 = input("enter player 1 name: ")
Player2 = input("enter player 2 name: ")
while(t < 2*NoofRound):
    if(Turn == 1):
        print(Player1 + " turn")
        MovieName = input("give movie name")

        ListofIndex = []
        print("enter index no. which you want to display")
        Index = 0
        while(Index != -1):
            Index = int(input("enter -1 to exit"))
            ListofIndex.append(Index)
        del ListofIndex[len(ListofIndex)-1]

    #we have to show space in movie name given to opponent. 
        for Space in range(len(MovieName)):
            if(MovieName[Space] == " "):
                ListofIndex.append(Space)
                
    #GuessString is the string which contain successfully guessed char. by opponent and character which player want to display for hint.
        GuessString = ""
        for i in ListofIndex:
            GuessString += MovieName[i]
            
    #user can enter max. 9 wrong attempt because bollywood and hollywood have 9 char.
        Attempt = 9
        print(Player2 +", you have 9 wrong attempt")
        while(Attempt > 0):
            
            #this for loop going to display char. of hint and successfully guessed by opponent.
              for i in range(len(MovieName)):
                  if(MovieName[i] == " "):
                      print(" ", end = "  ")
                  elif(i in ListofIndex):
                      print(MovieName[i] , end = " ")
                  else:
                      print("_" , end=" ")
              print("")
            
              c = input("enter a character: ")
              if(c in MovieName):
                    print("voila!! you got that")

                #this for loop is going to find index of entered char. by opponent.
                    for i in range(len(MovieName)):
                        if(c == MovieName[i]):
                            if(i not in ListofIndex):
                                ListofIndex.append(i)
                                GuessString += MovieName[i]
                                
                    print("GuessString : ",GuessString)
                    print("MovieName : ",MovieName)
                    
                #this if statement to see whether opponent win or not 
                    if(sorted(GuessString) == sorted(MovieName)):
                      print("CONGRATULATIONS" , Player2)
                      Player2Rank += Attempt
                      break
              else:
                  Attempt -= 1
                  print("you failed")
                  print("you have",str(Attempt),"attempt remaining")
        Turn = 2
    else:
        print(Player2 + " turn")
        MovieName = input("give movie name")

        ListofIndex = []
        print("enter index no. which you want to display")
        Index = 0
        while(Index != -1):
            Index = int(input("enter -1 to exit"))
            ListofIndex.append(Index)
        del ListofIndex[len(ListofIndex)-1]

    #we have to show space in movie name given to opponent. 
        for Space in range(len(MovieName)):
            if(MovieName[Space] == " "):
                ListofIndex.append(Space)
                
    #GuessString is the string which contain successfully guessed char. by opponent and character which player want to display for hint.
        GuessString = ""
        for i in ListofIndex:
            GuessString += MovieName[i]
            
    #user can enter max. 9 wrong attempt because bollywood and hollywood have 9 char.
        Attempt = 9
        print(Player1 +", you have 9 wrong attempt")
        while(Attempt > 0):
            
            #this for loop going to display char. of hint and successfully guessed by opponent.
              for i in range(len(MovieName)):
                  if(MovieName[i] == " "):
                      print(" ", end = "  ")
                  elif(i in ListofIndex):
                      print(MovieName[i] , end = " ")
                  else:
                      print("_" , end=" ")
              print("")
            
              c = input("enter a single character: ")
              if(c in MovieName):
                    print("aye!! you got that")

                #this for loop is going to find index of entered char. by opponent.
                    for i in range(len(MovieName)):
                        if(c == MovieName[i]):
                            if(i not in ListofIndex):
                                ListofIndex.append(i)
                                GuessString += MovieName[i]

                    
                    print("GuessString : ",GuessString)
                    print("MovieName : ",MovieName)
                
                #this if statement to see whether opponent win or not 
                    if(sorted(GuessString) == sorted(MovieName)):
                      print("CONGRATULATIONS" , Player1)
                      Player1Rank += Attempt
                      break
              else:
                  Attempt -= 1
                  print("you failed")
                  print("you have",str(Attempt),"attempt remaining")
        Turn = 1
        
    print(Player1 , ":   " , Player1Rank)
    print(Player2 , ":   " , Player2Rank)
    t+=1

if(Player1Rank > Player2Rank):
    print(Player1 , "WON!!!")
    print(Player1 , "beats" , Player2 , "by" , str(Player1Rank-Player2Rank) , "points.")
elif(Player1Rank < Player2Rank):
    print(Player2 , "WON!!!")
    print(Player2 , "beats" , Player1 , "by" , str(Player2Rank-Player1Rank) , "points.")
else:
    print("DRAW !!")
