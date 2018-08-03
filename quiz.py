import sys

print "Welcome to D.C.! Here's a fill in the blanks quiz to test your knowledge about the Capitol! \n"

print "Answers are case sensitive! \n"

quiz = "Washington D.C. is the Capitol of America, and it was founded in ____1____. its most prominent feature is the ____2____, which houses the president, and it is situated on ____3____ Avenue. The only president to have not resided within the White House during his tenure is ____4____. Like his namesake, the ____5____ is also the tallest building in town, as no building is allowed to exceed its height. Outside of that monument, D.C. also has monuments and memorials dedicated to ____6____, Eisenhower, ____7____, and ____8____. On average, an estimated 15 million tourists come to D.C. to visit its numerous cultural and historical locations. We encourage you to visit too!"

quiz_answers = ["1790", "White House", "Pennsylvania", "George Washington", "Washington Monument", "Lincoln", "Roosevelt", "Jefferson"]

answer_blank = ["____1____", "____2____", "____3____", "____4____", "____5____", "____6____", "____7____", "____8____"]

easy_lives = 5

medium_lives = 4

hard_lives = 3

def easy_quiz():
    print ("\n Good luck! You have 5 attempts! \n")
    print quiz
    return easy_lives

def medium_quiz():
    print ("\n Good luck! You have 4 attempts! \n")
    print quiz
    return medium_lives

def hard_quiz():
    print ("\n Good luck! You have 3 attempts! \n")
    print quiz
    return hard_lives

def choose_difficulty():
    selection = raw_input("Please select difficulty: Easy, Medium, Hard ")
    if selection == "Easy":
        return easy_quiz()
    if selection == "Medium":
        return medium_quiz()
    if selection == "Hard":
        return hard_quiz()
    else:
        if selection not in ("Easy", "Medium", "Hard"):
            print ("\n Please choose an approved quiz! \n")
            return choose_difficulty()


def play():
    lives = choose_difficulty()
    answer_blank_index = 0
    quiz_answers_index = 0
    quiz_1 = quiz

    while answer_blank_index < len(answer_blank):
        user_input = raw_input("Answer for " + answer_blank[answer_blank_index] + " :" + " " )
        if user_input == quiz_answers[quiz_answers_index]:
            print "\n Spot On! \n"
            quiz_1 = quiz_1.replace(answer_blank[answer_blank_index], user_input)
            print quiz_1
            quiz_answers_index += 1
            answer_blank_index += 1
            lives = lives
            if answer_blank_index == len(answer_blank):
                print "\n Winner! \n"
                play_again = raw_input("Play Again? Y/N: ")
                if play_again == "Y":
                    play()
                if play_again == "N":
                    print "\n Thanks for playing! \n"
                    sys.exit()
        else:
            print "\n Incorrect! You have " + str(lives - 1) + " chances remaining. \n"
            lives -= 1
            if lives == 0:
                print "\n You Lose! \n"
                try_again = raw_input("Try Again? Y/N: ")
                if try_again == "Y":
                    play()
                if try_again == "N":
                    print "\n Thanks for playing! \n"
                    sys.exit()

play()
