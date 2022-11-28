import pytholog as pl
import random
from knowledgeBase import kb

# GLOBALS
# question list
questions = [
    "Do you live near UABC?",

    # Systems
    "As a kid, did you like fixing and playing the PC's programs, or opening up and see what's inside of your toys, machines, appliances, etc?",
    "Do you like playing retrogames in emulators and tinkering with the settings?",

    # Industrial
    "Did you ever work at a factory in your life or are you working in one currently?",
    "Have you played with 3D modelling, like blender or maya, with 3D printers, or made 2D blueprints using CAD software?",

    # TICs
    "Have you ever made a podcast for school or personal use, or like to listen to them?",
    "Do you like to follow the news closely, in different mediums such as radio, news websites, etc?",

    # Mechanics
    "Do you like cars and how they work and look?",
    "Are you curious to know how internal combustion engines work?"
]

questions2 = [
    {"question": "Do you live near UABC?", "majors": ["systems", "tics"]},

    # Systems
    {"question": "As a kid, did you like fixing and playing the PC's programs, or opening up and see what's inside of your toys, machines, appliances, etc?",
        "majors": ["systems", "tics"]},
    {"question": "Do you like playing retrogames in emulators and tinkering with the settings?",
        "majors": ["systems", "tics"]},

    # Industrial
    {"question": "Did you ever work at a factory in your life or are you working in one currently?",
        "majors": ["industrial"]},
    {"question": "Have you played with 3D modelling, like blender or maya, with 3D printers, or made 2D blueprints using CAD software?",
        "majors": ["industrial", "mechanics"]},

    # TICs
    {"question": "Have you ever made a podcast for school or personal use, or like to listen to them?",
        "majors": ["tics"]},
    {"question": "Do you like to follow the news closely, in different mediums such as radio, news websites, etc?",
        "majors": ["tics"]},

    # Mechanics
    {"question": "Do you like cars and how they work and look?",
        "majors": ["mechanics"]},
    {"question": "Are you curious to know how internal combustion engines work?",
        "majors": ["mechanics"]},

]

# majors variables
tomasAquino = {
    "systems": 0,
    "tics": 0
}
otay = {
    "industrial": 0,
    "mechanics": 0
}

# Test lines
# tomasAquino = kb.query(pl.Expr("available_at_campus(X, tomasaquino)"))
# otay = kb.query(pl.Expr("available_at_campus(X, otay)"))

# print(tomasAquino)
# print(otay)


def questionLoop():
    while len(questions2) > 0:
        index = random.randint(0, len(questions2)-1)
        showQuestion(index)
        questions2.pop(index)


def showQuestion(index):
    # Show the question at index, from key "question"
    answer = input(questions2[index].get("question") + "\n")

    # Evaluate answer and add up points    
    if(answer == "yes" ):
        for major in questions2[index].get("majors"):
              if major in tomasAquino: 
                  num = tomasAquino[major]
                  num += 1
                  tomasAquino[major] = num
                  
              elif major in otay:
                  num = otay[major]
                  num += 1
                  otay[major] = num

    elif (answer == "no"):
        pass
        
    else:
        print("Answer just yes or no.")
        showQuestion(index)

def init():
    questionLoop()

init()
