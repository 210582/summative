import time
score=0
def introduction():
    name = input("Hi! What's your name?")
    print(name,"...")
    time.sleep(1)
    print("""
                            __      __          _                                       _
                        \ \    / / ___     | |     __      ___    _ __     ___     | |
                         \ \/\/ / / -_)    | |    / _|    / _ \  | '  \   / -_)    |_|
                          \_/\_/  \___|   _|_|_   \__|_   \___/  |_|_|_|  \___|   _(_)_
                        _|''''''|_|''''|_|'''''|_|'''''|_|'''''|_|''''''|_|''''|_|'''''|
                        "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'
                                                                                                           """)
    time.sleep(2)
    print("For each question, there are 4 choices. You can either choose 1, 2, 3, or 4.")
    time.sleep(1)
    print("There are 15 questions, and in the end, I will show you your score.")
    ready = 0
    time.sleep(2)
    while ready != "yes" and "no":
        ready = input("Are you ready?")
        if ready.lower() == "yes":
            print("Let's start!")
            question1()
        elif ready.lower() == "no":
            print("Well too bad.")
            question1()
        else:
            print("Choice not recognized.")


def question1():
    global score
    time.sleep(2)
    answer1 = 0
    while answer1 != "1" and "2" and "3" and "4":
        answer1 = input("Question 1: Grand Central Terminal, Park Avenue, New York is the world's "
                        "\n1.) Largest railway station"
                        "\n2.) Highest railway station"
                        "\n3.) Longest railway station"
                        "\n4.) None of the above")
        if answer1 == "1":
            print("Correct!")
            score = score+1
            question2()
        elif answer1 == "2" or "3" or "4":
            print("Wrong! The answer is 1.) Largest railway station")
            score = score+0
            question2()
        else:
            print("Answer not recognized.")

def question2():
    global score
    time.sleep(2)
    answer2 = 0
    while answer2 != "1" and "2" and "3" and "4":
        answer2 = input("Question 2: Entomology is the science that studies"
                        "\n1.) Behavior of human beings"
                        "\n2.) Insects"
                        "\n3.) The origin and history of technical and scientific terms"
                        "\n4.) The formation of rocks")
        if answer2 == "1" or "3" or "4":
            print("Wrong! Entomology is the science that studies insects")
            score = score+0
            question3()
        elif answer2 == "2":
            print("Correct!")
            score = score+1
            question3()
        else:
            print("Answer not recognized.")

def question3():
    global score
    time.sleep(2)
    answer3 = 0
    while answer3 != "1" and "2" and "3" and "4":
        answer3 = input("Question 3: Eritrea, which became the 182nd member of the UN in 1993, "
                        "is in the continent of"
                        "\n1.)Asia"
                        "\n2.)Africa"
                        "\n3.)Europe"
                        "\n4.)Australia")
        if answer3 == "1" or "3" or "4":
            print("Wrong! Eritrea is in Africa.")
            score = score+0
            question4()
        elif answer3 == "2":
            print("Correct!")
            score = score+1
            question4()
        else:
            print("Answer not recognized.")

def question4():
    global score
    time.sleep(2)
    answer4 = 0
    while answer4 != "1" and "2" and "3" and "4":
        answer4 = input("Question 4: Garampani sanctuary is located at"
                        "\n1.)Junagarh, Gujarat"
                        "\n2.)Diphu, Assam"
                        "\n3.)Kohima, Nagaland"
                        "\n4.)Gangtok, Sikkim")
        if answer4 == "1" or "3" or "4":
            print("Wrong! Garampani sanctuary is located at Diphu, Assam")
            score = score+0
            question5()
        elif answer4 == "2":
            print("Correct!")
            score = score+1
            question5()
        else:
            print("Answer not recognized.")

def question5():
    global score
    time.sleep(2)
    answer5 = 0
    while answer5 != "1" and "2" and "3" and "4":
        answer5 = input("Question 5: For which of the following disciplines is Nobel Prize awarded?"
                        "\n1.)Physics and Chemistry"
                        "\n2.)Physiology or Medicine"
                        "\n3.)Literature, Peace, and Economics"
                        "\n4.)All of the above")
        if answer5 == "1" or "2" or "3":
            print("Wrong! The answer is 'All of the above'.")
            score = score+0
            question6()
        elif answer5 == "4":
            print("Correct!")
            score = score+1
            question6()
        else:
            print("Answer not recognized.")

def question6():
    global score
    time.sleep(2)
    answer6 = 0
    while answer6 != "1" and "2" and "3" and "4":
        answer6 = input("Question 6: Hitler party which came into power in 1933 is known as?"
                        "\n1.)Labour Party"
                        "\n2.)Nazi Party"
                        "\n3.)Ku-Klux-Klan"
                        "\n4.)Democratic Party")
        if answer6 == "1" or "3" or "4":
            print("Wrong! Hitler party came into power as the Nazi Party.")
            score = score+0
            question7()
        elif answer6 == "2":
            print("Correct!")
            score = score+1
            question7()
        else:
            print("Answer not recognized.")

def question7():
    global score
    time.sleep(2)
    answer7 = 0
    while answer7 != "1" and "2" and "3" and "4":
        answer7 = input("Question 7: FFC stands for"
                        "\n1.)Foreign Finance Corporation"
                        "\n2.)Film Finance Corporation"
                        "\n3.)Federation of Football Council"
                        "\n4.)None of the above")
        if answer7 == "1" or "3" or "4":
            print("Wrong! FFC stands for Film Finance Corporation.")
            score = score+0
            question8()
        elif answer7 == "2":
            print("Correct!")
            score = score+1
            question8()
        else:
            print("Answer not recognized.")

def question8():
    global score
    time.sleep(2)
    answer8 = 0
    while answer8 != "1" and "2" and "3" and "4":
        answer8 = input("Question 8: Fastest shorthand writer was"
                        "\n1.)Dr. G. D. Bist"
                        "\n2.)J.R.D. Tata"
                        "\n3.)J.M. Tagore"
                        "\n4.)Khudada Khan")
        if answer8 == "1":
            print("Correct!")
            score = score+1
            question9()
        elif answer8 == "2" or "3" or "4":
            print("Wrong! The fastest shorthand writer was Dr G. D. Bist.")
            score = score+0
            question9()
        else:
            print("Answer not recognized.")

def question9():
    global score
    time.sleep(2)
    answer9 = 0
    while answer9 != "1" and "2" and "3" and "4":
        answer9 = input("Question 9: Epsom (England) is the place associated with"
                        "\n1.)Horse racing"
                        "\n2.)Polo"
                        "\n3.)Shooting"
                        "\n4.)Snooker")
        if answer9 == "1":
            print("Correct!")
            score = score+1
            question10()
        elif answer9 == "2" or "3" or "4":
            print("Wrong! Epsom is associated with horse racing.")
            score = score+0
            question10()
        else:
            print("Answer not recognized.")

def question10():
    global score
    time.sleep(2)
    answer10 = 0
    while answer10 != "1" and "2" and "3" and "4":
        answer10 = input("Question 10: First human heart transplant operation conducted by "
                         "Dr. Christiaan Barnard on Louis Washkansky, was conducted in"
                         "\n1.)1967"
                         "\n2.)1968"
                         "\n3.)1958"
                         "\n4.)1922")
        if answer10 == "1":
            print("Correct!")
            score = score+1
            question11()
        elif answer10 == "2" or "3" or "4":
            print("Wrong! The first human heart transplat was conducted in 1967.")
            score = score+0
            question11()
        else:
            print("Answer not recognized.")

def question11():
    global score
    time.sleep(2)
    answer11 = 0
    while answer11 != "1" and "2" and "3" and "4":
        answer11 = input("Question 11: Galileo was an Italian astronomer who"
                         "\n1.)Developed the telescope"
                         "\n2.)Discovered four satellites of Jupiter"
                         "\n3.)Discovered that the movement of pendulum produces a regular time"
                         "measurement"
                         "\n4.)All of the above")
        if answer11 == "1" or "2" or "3":
            print("Wrong! The answer is 'All of the above'.")
            score = score+0
            question12()
        elif answer11 == "4":
            print("Correct!")
            score = score+1
            question12()
        else:
            print("Answer not recognized.")

def question12():
    global score
    time.sleep(2)
    answer12 = 0
    while answer12 != "1" and "2" and "3" and "4":
        answer12 = input("Question 12: Habeas Corpus Act 1679"
                         "\n1.)States that no one was to be inprisoned without a writ or "
                         "warrant stating the charge against him"
                         "\n2.)provided facilities to a prisoner to obtain either speedy"
                         "trial or release in bail"
                         "\n3.)Safeguarded the personal liberties of the people against "
                         "arbitrary imprisonment by the king's orders"
                         "\n4.) All of the above")
        if answer12 == "1" or "2" or "3":
            print("Wrong! The answer is 'All of the above'.")
            score = score+0
            question13()
        elif answer12 == "4":
            print("Correct!")
            score = score+1
            question13()
        else:
            print("Answer not recognized.")

def question13():
    global score
    time.sleep(2)
    answer13 = 0
    while answer13 != "1" and "2" and "3" and "4":
        answer13 = input("Question 13: Exposure to sunlight helps a person improve his health"
                         "because"
                         "\n1.)The infrared light kills bacteria in the body"
                         "\n2.)Resistance power increases"
                         "\n3.)The pigment cells in the skin get stimulated and produce a"
                         "healthy tan"
                         "\n4.)The ultraviolet rays convert skin oil into Vitamin D")
        if answer13 == "1" or "2" or "3":
            print("Wrong! Exposre to sunlight helps improve healthy because the ultraviolet"
                  "rays convert skin oil into Vitamin D.")
            score = score+0
            question14()
            score = score+0
            question14()
        elif answer13 == "4":
            print("Correct!")
            score = score+1
            question14()
        else:
            print("Answer not recognized.")

def question14():
    global score
    time.sleep(2)
    answer14 = 0
    while answer14 != "1" and "2" and "3" and "4":
        answer14 = input("Question 14: Golf player Vijay Singh belongs to which country?"
                         "\n1.)USA"
                         "\n2.)Fiji"
                         "\n3.)India"
                         "\n4.)UK")
        if answer14 == "1" or "3" or "4":
            print("Wrong! Vijay Singh comes from Fiji.")
            score = score+0
            question15()
        elif answer14 == "2":
            print("Correct!")
            score = score+1
            question15()
        else:
            print("Answer not recognized.")

def question15():
    global score
    time.sleep(2)
    print("Last question!")
    answer15 = 0
    while answer15 != "1" and "2" and "3" and "4":
        answer15 = input("Question 15: First Afghan War took place in"
                         "\n1.)1833"
                         "\n2.)1843"
                         "\n3.)1839"
                         "\n4.)1848")
        if answer15 == "1" or "2" or "4":
            print("Wrong! The First Afghan War took place in 1839.")
            score = score+0
            ending()
        elif answer15 == "3":
            print("Correct!")
            score = score+1
            ending()
        else:
            print("Answer not recognized.")

def ending():
    global score
    import sys
    print("You have completed my quiz!")
    time.sleep(1)
    print("Here is your score:", score, "/15")
    if 0<=score<=5:
        print("You need to work harder...")
    elif 6<=score<=10:
        print("Eh...You can do better!")
    elif 11<=score<=14:
        print("Ooh...Not too bad!")
    else:
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

