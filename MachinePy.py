import socket
players = ["Roxi", "Mat", "Ana"]
class Player:
    def __init__(self, username, house):
        self.username = username
        self.house = house
class Werewolf(Player):
    def __init__(self, username, house):
        super().__init__(username, house)
    def printstuff(self):
        print(self.username, self.house, self.kill)
    def Kill(self):
        while True:
            actualPlayer = False
            target = input("Choose a player to kill\n")
            for loser in players:
                if target == loser:
                    print("You Killed " + loser)
                    actualPlayer = True
                    players.remove(loser)
            if actualPlayer == False:
                print("Not an actual player")
            if actualPlayer == True:
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
x = Werewolf(q, 2)
x.Kill()
print("Remaining Survivors:")
print(players)
while True:
    realPlayer = False
    vote = input("Choose someone to vote out\n")
    for loser in players:
        if loser == vote:
            print(loser + " has been voted out!")
            players.remove(loser)
            realPlayer = True
    if realPlayer == False:
        print("Not a real player.")
    if realPlayer == True:
        break
print("Remaining Survivors:")
print(players)

