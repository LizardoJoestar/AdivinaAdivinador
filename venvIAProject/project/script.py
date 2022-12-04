import pytholog as pl
import random
from knowledgeBase import kb
from questionList import questions2 as qList

# majors variables
tomasAquino = {
    "systems": 0,
    "tics": 0
}
otay = {
    "industrial": 0,
    "mechanics": 0
}


def questionLoop():
    while len(qList) > 0:
        index = random.randint(0, len(qList)-1)
        showQuestion(index)
        qList.pop(index)


def showQuestion(index):
    # Show the question at index, from key "question"
    answer = input(qList[index].get("question") + "\n")

    # Evaluate answer and add up points
    if (answer == "yes"):
        for major in qList[index].get("majors"):
            if major in tomasAquino:
                tomasAquino[major] += 1

            elif major in otay:
                otay[major] += 1

    elif (answer == "no"):
        pass

    else:
        print("Answer just yes or no.")
        showQuestion(index)


def showPoints():
    """
    For debugging; prints the points total of each major of each
    campus
    """
    print("\n")
    for major in tomasAquino:
        print(major, ":", tomasAquino[major])

    for major in otay:
        print(major, ":", otay[major])


def getRecommended():
    recommended = []
    maximum = 0

    # Find the major with the most points. Stores just one
    for major in tomasAquino:
        if tomasAquino[major] > maximum:
            maximum = tomasAquino[major]

            # If recommended already has an item, remove it and store the
            # new one. This ensures there's always just one item in recommended
            if len(recommended) != 0:
                recommended.pop()
                recommended.append(major)
            else:
                recommended.append(major)

    for major in otay:
        if otay[major] > maximum:
            maximum = otay[major]

            if len(recommended) != 0:
                recommended.pop()
                recommended.append(major)
            else:
                recommended.append(major)

    # First check if the singular item in recommended is in any
    # of the majors list (tomasAquino or otay)
    if recommended[0] in tomasAquino:
        for major in tomasAquino:
            # First conditional avoids a duplicate major in recommended
            # Second conditional compares their points. If equal, add such
            # major to recommended too
            if major != recommended[0] and tomasAquino[major] == tomasAquino[recommended[0]]:
                recommended.append(major)

    elif recommended[0] in otay:
        for major in otay:
            if major != recommended[0] and otay[major] == otay[recommended[0]]:
                recommended.append(major)

    return recommended


def report():
    print(getRecommended())


def init():
    questionLoop()
    showPoints()
    report()


init()
