import time     #I imported time in the beginning of the program so I
                # can use the time.sleep function in my questions
score=0         #I created the variable score and set it to the value of 0


def introduction(): #This is the introduction function
    print("""
                            __      __          _                                       _
                        \ \    / / ___     | |     __      ___    _ __     ___     | |
                         \ \/\/ / / -_)    | |    / _|    / _ \  | '  \   / -_)    |_|
                          \_/\_/  \___|   _|_|_   \__|_   \___/  |_|_|_|  \___|   _(_)_
                        _|''''''|_|''''|_|'''''|_|'''''|_|'''''|_|''''''|_|''''|_|'''''|
                        "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'
                                                                                                           """)
    time.sleep(2)
    print("For each question you can either choose t for true, or f for false.") #Here I'm explaining the game
    time.sleep(1)
    print("There are 15 questions, and in the end, I will show you your score.")
    ready = 0
    time.sleep(2)
    while ready != "yes" and "no": #A short question and response before the actual game
        ready = input("Are you ready?")
        if ready.lower() == "yes":
            print("Let's start!")
            question10()
        elif ready.lower() == "no":
            print("Well too bad.")
            question10()
        else:
            print("Choice not recognized.")


def question1():
    global score
    time.sleep(2)
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
    global lines
    print(lines[4])
    wronganswer = lines[5]
    x = input()
    if x.lower() is not wronganswer:
        score += 1
        print("Correct!")
        question4()
    else:
        print("Wrong!")
        question4()

def question4():
    global score
    global lines
    print(lines[6])
    wronganswer = lines[7]
    x = input()
    if x.lower() is not wronganswer:
        score += 1
        print("Correct!")
        question4()
    else:
        print("Wrong!")
        question4()


def question5():
    global score
    global lines
    print(lines[8])
    wronganswer = lines[9]
    x = input()
    if x.lower() is not wronganswer:
        score += 1
        print("Correct!")
        question4()
    else:
        print("Wrong!")
        question4()

def question6():
    global score
    time.sleep(2)
    answer6 = 0
    while answer6 != "t" and "f":
        answer6 = input("Question 6: Is Au the chemical symbol for gold?"
                        "\nPress t for true, f for false")
        if answer6 == "t":
            print("Correct! Au is the chemical symbol for gold.")
            score = score+1
            question7()
        elif answer6 == "f":
            print("Wrong! Au is the chemical symbol for gold.")
            score = score+0
            question7()
        else:
            print("Answer not recognized.")

def question7():
    global score
    time.sleep(2)
    answer7 = 0
    while answer7 != "t" and "f":
        answer7 = input("Question 7: Do eagles nest in an eyrie?"
                        "\nPress t for true, f for false")
        if answer7 == "t":
            print("Correct! Eagles nest in an eyrie.")
            score = score+1
            question8()
        elif answer7 == "f":
            print("Wrong! Eagles nest in an eyrie.")
            score = score+0
            question8()
        else:
            print("Answer not recognized.")

def question8():
    global score
    time.sleep(2)
    answer8 = 0
    while answer8 != "t" and "f":
        answer8 = input("Question 8: Is your coccyx in your ear?"
                        "\nPress t for true, f for false")
        if answer8 == "t":
            print("Wrong! Your coccyx is at the base of your spine.")
            score = score+0
            question9()
        elif answer8 == "f":
            print("Correct! Your coccyx is at the base of your spine.")
            score = score+1
            question9()
        else:
            print("Answer not recognized.")

def question9():
    global score
    time.sleep(2)
    answer9 = 0
    while answer9 != "t" and "f":
        answer9 = input("Question 9: Did the Iron Age precede the Bronze Age?"
                        "\nPress t for true, f for false")
        if answer9 == "t":
            print("Wrong! The Iron Age followed the Bronze Age.")
            score = score+0
            question10()
        elif answer9 == "f":
            print("Correct! THe Iron Age followed the Bronze Age.")
            score = score+1
            question10()
        else:
            print("Answer not recognized.")

def question10():
    global score
    time.sleep(2)
    answer10 = 0
    while answer10 != "t" and "f":
        answer10 = input("Question 10: Does the Suez Canal connect the Mediterranean and the Red Sea?"
                         "\nPress t for true, f for false")
        if answer10 == "t":
            print("Correct! The Suez Canal does connect the Mediterranean and the Red Sea.")
            score = score+1
            question11()
        elif answer10 == "f":
            print("Wrong! The Suez Canal does connect the mediterranean and the Red Sea.")
            score = score+0
            question11()
        else:
            print("Answer not recognized.")

def question11():
    global score
    time.sleep(2)
    answer11 = 0
    while answer11 !="t" and "f":
        answer11 = input("Question 11: Is gannet a type of bird?"
                         "\nPress t for true, f for false")
        if answer11 == "t":
            print("Correct! Gannet is a type of bird.")
            score = score+1
            question12()
        elif answer11 == "f":
            print("Wrong! Gannet is a type of bird.")
            score = score+0
            question12()
        else:
            print("Answer not recognized.")

def question12():
    global score
    time.sleep(2)
    answer12 = 0
    while answer12 != "t" and "f":
        answer12 = input("Question 12: Does a philatelist collect coins?"
                         "\nPress t for true, f for false")
        if answer12 == "t":
            print("Wrong! A philatelist collects stamps.")
            score = score+0
            question13()
        elif answer12 == "f":
            print("Correct! A philatelist collects stamps.")
            score = score+1
            question13()
        else:
            print("Answer not recognized.")

def question13():
    global score
    time.sleep(2)
    answer13 = 0
    while answer13 != "t" and "f":
        answer13 = input("Question 13: Is Leonardo Da Vinci's 'Mona Lisa' on display at the Louvre, Paris,"
                         "\nPress t for true, f for false")
        if answer13 == "t":
            print("Correct! 'Mona Lisa' is on display at the Louvre.")
            score = score+1
            question14()
        elif answer13 == "f":
            print("Wrong! 'Mona Lisa' is on display at the Louvre.")
            score = score+0
            question14()
        else:
            print("Answer not recognized.")

def question14():
    global score
    time.sleep(2)
    answer14 = 0
    while answer14 != "t" and "f":
        answer14 = input("Question 14: Does mohair come from sheep?"
                         "\nPress t for true, f for false")
        if answer14 == "t":
            print("Wrong! Mohair comes from goats.")
            score = score+0
            question15()
        elif answer14 == "f":
            print("Correct! Mohair comes from goats.")
            score = score+1
            question15()
        else:
            print("Answer not recognized.")

def question15():
    global score
    time.sleep(2)
    print("Last question!")
    answer15 = 0
    while answer15 != "t" and "f":
        answer15 = input("Question 15: Does the Roman numeral M stand for 1000?"
                         "\nPress t for true, f for false")
        if answer15 == "t":
            print("Correct! The Roman numeral M stands for 1000.")
            score = score+1
            ending()
        elif answer15 == "f":
            print("Wrong! The Roman numeral M stands for 1000.")
            score = score+1
            ending()
        else:
            print("Answer not recognized.")

def ending(): #This is the ending function
    global score #Globalising score allows me to print the variable 'score' that has been the same used in
    #previous functions
    import sys
    print("You have completed my quiz!")
    time.sleep(1)
    print("Here is your score:", score, "/15") #This prints the score /15, which is how many questions there are
    if 0<=score<=5: #If the user gets 0 to 5 questions correct, it will print:
        print("You need to work harder...")
    elif 6<=score<=10: #If the user gets 6 to 10 questions to correct, it will print:
        print("Eh...You can do better!")
    elif 11<=score<=14: #If the user gets 11 to 14 questions correct, it will print:
        print("Ooh...Not too bad!")
    else: #Else meaning that if the user gets all of the question correct, it will print:
        print("""Nice! You got 100%! Here is an A+:





                                           AAA
                                          AAAAA
                                         AAAAAAA
                                        AAAAAAAAA                   +++++++
                                       AAAAAAAAAAA                  +++++++
                                      AAAAAAAAAAAAA                 +++++++
                                     AAAAAAA AAAAAAA          +++++++++++++++++++
                                    AAAAAAA   AAAAAAA         +++++++++++++++++++
                                   AAAAAAA     AAAAAAA        +++++++++++++++++++
                                  AAAAAAAAAAAAAAAAAAAAA       +++++++++++++++++++
                                 AAAAAAAAAAAAAAAAAAAAAAA            +++++++
                                AAAAAAAAAAAAAAAAAAAAAAAAA           +++++++
                               AAAAAAA             AAAAAAA          +++++++
                              AAAAAAA               AAAAAAA
                             AAAAAAA                 AAAAAAA
                            AAAAAAA                   AAAAAAA






        """)
    time.sleep(2)
    print("Thanks for playing my game!")
    sys.exit()






introduction()
#This is the main program, because at the end of each function it calls the next one, this is the only function
#I need to call

