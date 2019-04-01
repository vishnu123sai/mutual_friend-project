from django.shortcuts import render
import random
import os
from mutual_friends import settings

# Create your views here.
def friendsList():
    list=[]
    file = open(os.path.join(settings.STATIC_ROOT, 'names.txt'))
    for a in file:
        list.append(a)
    return list

def frnds(friends):
    friends1=[]
    for i in range(15):
        a = random.randint(0,len(friends)-1)
        friends1.append(friends[a])

    return friends1



def index(request):
    friends = friendsList()
    friend1 = set(frnds(friends))
    friend2 = set(frnds(friends))
    mutual = []
    for i in friend1:
        if i in friend2:
            mutual.append(i)

    return render(request, 'index.html', context={'mutual': mutual , 'friend1' : list(friend1) , 'friend2': list(friend2) })
    
