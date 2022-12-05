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
    """
    Loop through a list of questions at random, without repetition.
    """
    while len(qList) > 0:
        index = random.randint(0, len(qList)-1)
        showQuestion(index)
        qList.pop(index)


def showQuestion(index):
    """
    Prints a question at index, accepts answer from user and increments or decrements points depending on the majors the question affects.
    """
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
    For debugging; prints the points total of each major of each campus.
    """
    print("\n")
    for major in tomasAquino:
        print(major, ":", tomasAquino[major])

    for major in otay:
        print(major, ":", otay[major])


def getRecommended():
    """
    Returns a list of the recommended majors, i.e., those with the most points.
    If more than one major have the same points, put them all in the list.
    """
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


def checkSameCampus(recommended):
    """
    Returns a filtered list of the recommended majors list passed in.
    If the list is just one element, return the same list.
    If the list has more than one element, return just those in the same campus.
    If the filtered list didn't get any results (size is 0), return the same list.
    """
    filteredRec = []

    if len(recommended) > 1:
        for i in range(len(recommended)):
            for j in range(len(recommended)):
                same_campus = kb.query(
                    pl.Expr(f"same_campus({recommended[i]},{recommended[j]})"))

                if same_campus[0] == 'Yes':
                    if recommended[i] not in filteredRec:
                        filteredRec.append(recommended[i])
                    if recommended[j] not in filteredRec:
                        filteredRec.append(recommended[j])
    else:
        filteredRec.append(recommended[0])

    # If all majors are in different campuses, pass the recommended ones as is
    if len(filteredRec) == 0:
        for rec in recommended:
            filteredRec.append(rec)

    return filteredRec


def checkAlternatives(major):
    """
    Returns a list of alternative majors in the same campus, and that share some of the same tools and subjects.
    """
    # Query returns a list with just one item. So, select for index 0
    # and value of key X to get it
    campus = kb.query(pl.Expr(f"partof({major},X"))[0]['X']

    # This returns a list of dictionaries, each one with a single item
    temp1 = kb.query(pl.Expr(f"available_at_campus(X,{campus})"))

    # Filter the dictionary list to store only the values (majors in same campus)
    temp2 = []
    for item in temp1:
        temp2.append(item['X'])

    # Now compare this list of majors in same campus with first choice major
    # to know if they share the same tools or subjects
    alternatives = []
    for item in temp2:
        answer = kb.query(pl.Expr(f"use_same_tools({major},{item})"))

        if answer[0] == 'Yes':
            alternatives.append(item)

    return alternatives


def checkToolsUsed(recommended):
    """
    Returns a list of tools used per major in recommended list parameter.
    """
    toolsUsed = []

    for major in recommended:
        tools = kb.query(pl.Expr(f"uses({major},X"))
        for tool in tools:
            if tool['X'] not in toolsUsed:
                toolsUsed.append(tool['X'])

    return toolsUsed


def report():
    """
    Generates a report of recommended majors, alternative majors and relevant subjects/tools, based on user answers in previous question loop.
    """
    recommended = getRecommended()

    # This 3 functions make use of prolog queries, therefore making use of
    # (rudimentary) AI in the form of a knowledge base and the prolog inference
    # engine
    filteredRec = checkSameCampus(recommended)
    alternatives = checkAlternatives(filteredRec[0])
    toolsUsed = checkToolsUsed(filteredRec)

    print("\nEn base a tus respuestas, te recomendamos esta carrera(s):")
    for item in filteredRec:
        print(item)

    if len(alternatives) > 0:
        print("\nTambien te recomendamos estas carreras similares en el mismo campus:")
        for item in alternatives:
            print(item)

    print("\nY estos son los temas o herramientas relevantes a tu recomendación:")
    for item in toolsUsed:
        print(item)


def testing():
    """
    For testing purpouses
    """
    showPoints()
    print(getRecommended())


def init():
    # questionLoop() must always go first
    questionLoop()
    # testing()
    report()


init()
