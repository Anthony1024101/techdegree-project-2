from constants import TEAMS, PLAYERS
import copy


def clean_data(players):
    
    
    for player in players:
        player["height"] = int(player["height"][0:2])

        if player["experience"] == "YES":
            player["experience"] = True
        else:
            player["experience"] = False
            
    return players  

def balance_teams(players_list):
   global panthers, bandits, warriors
   experienced = []
   inexperienced = []
   panthers = []
   bandits = []
   warriors = []

   for player in players_list:
       if player["experience"] == True:
           experienced.append(player)
       else:
           inexperienced.append(player)

   for num, player in enumerate(experienced, start = 1):
       if num % 3 == 0:
           panthers.append(player)
       elif num % 2 == 0:
           bandits.append(player)
       else:
           warriors.append(player)

   for num, player in enumerate(inexperienced, start = 1):
       if num % 3 == 0:
           panthers.append(player)
       elif num % 2 == 0:
           bandits.append(player)
       else:
           warriors.append(player)

   return panthers, bandits, warriors


def display_info(team, players):
    exp_players = 0
    inexp_players = 0
    height = 0
    names_list = []
    

    for player in players:
        if player["experience"] is True:
            exp_players += 1
        elif player["experience"] is False:
            inexp_players += 1

        height += player["height"]
        names_list.append(player["name"])
        
   
    names = ", ".join([str(name) for name in names_list])
 
    print("\nStats for the {}.\n".format(team))
    print("{} players on the team.\n".format(len(players)))
    print("Players:", names, "\n")
  
        

def menu(TEAMS, players_list):
    clean_data(players_list)
    balance_teams(players_list)

    print("\nBasketBall Stats Tool!")
    print("\nPlease Select an Option from Below.")
    
    while True:
        print("\nA.) Panthers")
        print("B.) Bandits")
        print("C.) Warriors")
        print("D.) Exit\n")
        

        try:
            response = input("> ")

            if response.lower() == "a":
                display_info(TEAMS[0], panthers)
                continue
            elif response.lower() == "b":
                display_info(TEAMS[1], bandits)
                continue
            elif response.lower() == "c":
                display_info(TEAMS[2], warriors)
                continue
            elif response.lower() == "d":
                print("See you Later!")
                break
            else:
                raise ValueError()
        except ValueError as err:
            print("Please Select a Listed Option.")


if __name__ == "__main__":
    menu(TEAMS, copy.deepcopy(PLAYERS))
    
