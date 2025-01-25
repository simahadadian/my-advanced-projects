import random
mylist=[]
teamA=[]
teamB=[]
class Human:
    def __init__(self,name):
        self.name=name        
    def get_name(self):        
        mylist.append(self.name)

class Footballer(Human):
    pass

 
allplayer=input()
allplayer=allplayer.split('-')


for i in range(0,22):   
    player=Footballer(allplayer[i])    
    player.get_name()


while len(mylist)!=0:
    choose1=random.choice(mylist)
    teamA.append(choose1)
    mylist.remove(choose1)
    choose2=random.choice(mylist)
    teamB.append(choose2)
    mylist.remove(choose2)

for names in teamA:
    print(names,'A')
for names in teamB:
    print(names,'B')
