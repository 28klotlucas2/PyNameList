import requests
import random


def get_namelists(lists):
    names = []
    for i in lists:
        namelist = i

        for i in namelist:
            if i not in names:
                names.append(i)

    return names


def get_names(amount):
    names = []

    for i in range(1, amount + 1):
        choice = random.choice(range(1, len(namelist) + 1))

        names.append(namelist[choice - 1])
        
        namelist.remove(namelist[choice - 1])
      
    return names


namelists = [
    requests.get("https://web.archive.org/web/20200329092650if_/https://brutalmania.io/ndat.txt").text.split("\n"),
    requests.get("https://web.archive.org/web/20200329092648if_/https://evowars.io/nicki.txt").text.split("\n")
]

namelist = get_namelists(namelists)