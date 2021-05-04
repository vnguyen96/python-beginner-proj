print("Greeting warriror!") #print is syntax 

name = input("What is your name warrior? ") #store input in a variable called "name"

'''
if name.isdigit:
    print ("Please enter your name without a number")
else:
    print (name)
    '''

age = int(input("What is your age? ")) #store input in a variable called "age" 
#we want to store the input as int type because we going to need to compare age later on

print("Greeting", name, "I believe that you are", age, "years old") #print out variables name and age which stored input

##is_older = int(age) >= 18 
#int(age) convert age variable from string to an int type because we can't compare str to int

#is_older = age >= 18 
#store age >= expression into variable called "is_older"

if age >= 18:
    print("You are old enough to begin your adventure")

##elif age >= 14:
   ## print("You can play with supervision")

    heath = 10
    mana = 10 

    wants_to_play = input("Do you want start your adventure? ").lower() ## .lower() method conver input into all lower case 

    if wants_to_play == "yes":  ## this == expression basically checking the user input in wants_to_play
        print("Let's begin! You will start with", heath, "heath and", mana, "mana")

        left_or_right = input("As you walk on the path it suddently splits... Are you going Left or Right? (left/right)? " )

        if left_or_right == "left":
            claim_or_continue = input("You follow the path and reach a mountain... Do you want to climb or continue on your path? (climb/continue)? ")

            if claim_or_continue == "climb":
                fight_or_run = input("You have encountered a pack of wolves. Fight or Run (fight/run)? ")

            else:
                print ("As you continue to walk a rock fell on your head...")

        elif left_or_right == "right": 
            swim_or_continue = input("You follow the path and reach a lake... Do you want to swim or continue on your path? (swim/continue)? ")
            
            print("You got bitten by a water snake and lost 1 heath", heath, "your current heath is", heath)

            
    else:
        print("I'll be here if you change your mind")

else: 
    print("You are too young to play...:(")
























'''
These are 4 type of data:

string "hello", "hi" , "89"
int 8, 7, -1, 1000
float 6.0, 5.3, 32.2
bool True, False
'''