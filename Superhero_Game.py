#Game intro
villain_name = 'Bob'

print("CITIZEN: Oh, thank goodness you're here! " + villain_name
      + ' is destroying our city and we need your help to stop them!')

hero = input('What is your name, superhero?\n')

print("Welcome " + hero + "!")

points = 0

#Saving Mr Whiskers
print("CITIZEN: First things first: my darling cat Mr Whiskers is stuck up a tree!")
answer_1 = input("A: Did " + villain_name + " put him there?! \nB: On it! \n")

if answer_1 == "A" or answer_1 == "a":
    print("CITIZEN: Kind of? Mr Whiskers was out in the garden when the the sound of " + villain_name +
          " flying past startled him and caused him to climb up the tree!")
    answer_1 = input()

if answer_1 == "B" or answer_1 == "b":
    print("As you approach the citizen's house, you see a scared-looking white cat perched on top of a very frail-looking tree."+
         " Close to the tree, you spot two objects: a ladder and a saw.")
    answer_2 = input("Which do you pick? \n")
    
    if answer_2 == "ladder" or answer_2 == "Ladder":
        print(hero +": There's a ladder right there.")
        print("CITIZEN: Yeah, but it's broken. You can buy a new one from the shop next door - I'll give you the money - or" +
             " borrow one from Ms Smith, who lives two blocks away.")
        answer_3 = input("Type 'buy' to buy a ladder or 'borrow' to borrow one from Ms Smith. You can also type 'saw' to pick the saw \n")
        
        if answer_3 == "buy" or answer_3 == "Buy":
            print("The citizen gives you the money and you go buy a ladder from the shop. Using the new ladder, you" +
                 "successfully rescue Mr Whiskers from the tree.")
            points += 1
            
        elif answer_3 == "borrow" or answer_3 == "Borrow":
            print("CITIZEN: Great! I'll let you ride my car - unless you want to walk?")
            answer_4 = input("Type 'car' or 'walk'\n")
            
            if answer_4 == "walk" or answer_4 == "Walk":
                print("You walk to Ms Smith's house and borrow her ladder. You walk back to the citizen's house and" +
                     "succesfully rescue Mr Whiskers from the tree")
                points += 5
                
            elif answer_4 == "car" or answer_4 == "Car":
                print("You ride to Ms Smith's house and borrow her ladder. You ride back to the citizen's house and" +
                     "succesfully rescue Mr Whiskers from the tree")
                points += 3
                
            else:
                print("Please type 'car' or 'walk'")
        else:
            print("Please type 'buy', 'borrow' or 'saw'")
    
    if answer_2 == "saw" or answer_2 == "Saw" or answer_3 == "saw" or answer_3 == "Saw":
        print("Using the saw, you cut down the tree. As it falls, Mr Whiskers jumps to the ground and runs back inside the " +
             "citizen's house.")
        points = points - 5
        
    else:
        print("Please type 'ladder' or 'saw'")
           
    answer_5 = input("A: You know, you shouldn't really let your cat out of your house. It could get hit by cars, catch diseases and " +
         "kill the local wildlife.\nB: Task number one completed! See you later Mr Whiskers!\n")
    
    if answer_5 == "A" or answer_5 == "a":
        print("CITIZEN: You're right " + hero + ", I promise that from now on Mr Whiskers will stay inside.")
        points += 2
        print("Total score: " + str(points))
              
    elif answer_5 == "B" or answer_5 == "b":
        print("CITIZEN: You go " + hero + "!")
        print("Total score: " + str(points))
    else:
        print("Please type A or B")
    
    
else: 
    print("Please type A or B")
