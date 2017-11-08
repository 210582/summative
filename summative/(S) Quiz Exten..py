score = 0
def question1():
    global score
    f = open('tfquiz')
    lines = f.readlines()
    print(lines[0])
    x = input()
    if x == "f":
        score += 1
        print("Correct!")
        question2()
    elif x == "t":
        print("Wrong!")
        question2()
    else:
        print("Answer not recognized.")
        question1()


def question2():
    global score
    f = open('tfquiz')
    lines = f.readlines()
    print(lines[2])
    x = input()
    if x == "t":
        score += 1
        print("Correct!")
        question3()
    elif x == "f":
        print("Wrong!")
        question3()
    else:
        print("Answer not recognized.")
        question2()


def question3():
    global score
    f = open('tfquiz')
    lines = f.readlines()
    print(lines[2])
    x = input()
    if x == "t":
        score += 1
        print("Correct!")
        question4()
    elif x == "f":
        print("Wrong!")
        question4()
    else:
        print("Answer not recognized.")
        question3()

def question4():
    global score
    f = open('tfquiz')
    lines = f.readlines()
    print(lines[4])
    x = input()
    if x == "f":
        score += 1
        print("Correct!")
        question5()
    elif x == "t":
        print("Wrong!")
        question5()
    else:
        print("Answer not recognized.")
        question4()


def question5():
    global score
    f = open('tfquiz')
    lines = f.readlines()
    print(lines[6])
    x = input()
    if x == "f":
        score += 1
        print("Correct!")
        main()
    elif x == "t":
        print("Wrong!")
        main()
    else:
        print("Answer not recognized.")
        question5()


def gethighscore():
    high_score = 0
    try:
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        print("The high score is", high_score)
    except IOError:
        print("There is no high score yet.")
    except ValueError:
        print("Starting with no high score.")
    return high_score


def savehighscore(new_high_score):
    try:
        high_score_file = open("high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        print("Unable to save the high score.")


def main():
    global score
    high_score = gethighscore()

    if score > high_score:

        print("This is your score",score)
        print("Yea! New high score!")
        savehighscore(score)
    else:
        print("Your score is:",score,
              "\nBetter luck next time.")

question1()
