#author : Swapnasheel Sonkamble
#simple ROCK PAPER LIZARD SCISSORS SPOCK game
#try running on www.codeskulptor.org


from random import randrange


def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Such name doesn't exist"

  

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Number doesn't exist"
    


def rpsls(player_choice): 
    player_number = name_to_number(player_choice)
    comp_number = randrange(5)
    comp_choice = number_to_name(comp_number)
    
    print "Player's Choice is : " + player_choice
    print "Computer's Choice is : " + comp_choice
    
    if 1<=(player_number - comp_number) % 5<=2:
        print "Player wins!"
    elif (player_number - comp_number) % 5 > 2:
        print "Computer wins!"
    else:
        print "Player and computer tie!"
    
    print

    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



