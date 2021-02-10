import random
players = ["Roxi", "Mat", "Ana", "John"]
atStart = len(players)
alive = True
class Player:
    def __init__(self, username, house):
        self.username = username
        self.house = house
    def Vote(self):
        while True:
            realPlayer = False
            vote = input("Choose someone to vote out\n")
            for loser in players:
                if loser == vote:
                   unlucky = loser
                   print(loser + " has been voted out!")
                   players.remove(loser)
                   realPlayer = True
            if realPlayer == False:
                print("Not a real player.")
            if realPlayer == True:
                break
        print("Remaining Survivors:")
        print(players)
        print(werewolf)
        if unlucky == werewolf and not werewolf == q:
             print("You win!")
        if unlucky == werewolf and werewolf == q:
             print("You don't win")
        if not unlucky == werewolf and not werewolf == q:
             print("You LOSE")
        if not unlucky == werewolf and werewolf == q:
             print("You win!")

class Werewolf(Player):
    def __init__(self, username, house):
        global werewolf
        werewolf = q
        super().__init__(username, house)
    def Kill(self):
        print(players)
        while True:
            actualPlayer = False
            target = input("Choose a player to kill\n")
            for loser in players:
                if target == loser and not target == q:
                    print("You Killed " + loser)
                    actualPlayer = True
                    players.remove(loser)
            if actualPlayer == False:
                print("Not an actual player or you tried to kill yourself, which you obviously cannot do.")
            if actualPlayer == True:
                break

class Villager(Player):
    def __init__(self, username, house):
        super().__init__(username, house)
    def Investigate(self):
        who = random.randint(1, atStart)
        werewolfFound = False
        i = 1
        print(players)
        q = input("Choose a player to investigate\n")
        global werewolf
        for loser in players:
            if i == who:
                werewolf = loser
            i += 1
        if q == werewolf:
            print(werewolf + " is the werewolf")
        if not q == werewolf:
            print("you.are.WRONG!")
    def DeathChosen(self):
        while True:
            broken = False
            who = random.randint(1, atStart)
            i = 1
            for loser in players:
               if i == who and not loser == werewolf:
                  players.remove(loser)
                  print(loser + " has been killed! NOOOOOOOOOOOO!")
                  broken = True
               i += 1
            if broken == True:
                break



occ = False
while True:
    q = input("Choose a username\n")
    for loser in players:
        if loser == q:
            occ = True
    if occ == True:
        print("Username already exists.")
        occ = False
    elif occ == False:
        break
players.append(q)
do = input("Do you want to be a an innocent little Villager? or a BLOODTHIRSTY WEREWOLF?\n")
if do.lower() == "werewolf":
    x = Werewolf(q, 2)
    x.Kill()
    print("Remaining Survivors:")
    print(players)
    x.Vote()
if do.lower() == "villager":
    x = Villager(q, 2)
    x.Investigate()
    x.DeathChosen()
    x.Vote()
