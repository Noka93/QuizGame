# Prompt the user to enter a name
# Prompt the user to select an input to proceed with the quiz
# Using the selection statement, ask the user questions and then print result if user input is correct or false
# Calculate and print the total quiz scores
# Using loop ask the user if they want to continue and if yes, take them back to question else quit

name = input("Enter your name :\n")

print(f"Welcome {name} to your quiz game")

user_choice = int(input("Enter 1 to start : "))

if user_choice != 1:
    quit()


def quiz_game():

    scores = 0

    questions = input("Question 1:\nWhen did Nigeria get her Independence?\nA: 1994\nB: 1963\nC: 1988\nD: 1960\n")
    if questions.upper() == "D":
        print("Correct!")
        scores += 1
    else:
        print("Failed")

    questions = input("Question 2:\nWhat does BBC  stand for?\nA: Battery Backed Cache\nB: Broadband Conducted\n"
                      "C: British Broadcasting Corporation\nD: Broadband Content\n")
    if questions.upper() == "C":
        print("Correct!")
        scores += 1
    else:
        print("Failed")

    questions = input("Question 3:\nHow many days are in a leap year?\nA: 365\nB: 266\nC: 366\nD: 401\n")
    if questions.upper() == "C":
        print("Correct!")
        scores += 1
    else:
        print("Failed")

    questions = input("Question 4:\nIn meters, how long is an Olympic swimming pool?\nA: 50 Meters\n"
                      "B: 500 Meters\nC: 100 Meters\nD: 150 Meters\n")
    if questions.upper() == "A":
        print("Correct!")
        scores += 1
    else:
        print("Failed")

    questions = input("Question 5:\nWhat is the capital of Nigeria?\nA: Lagos\nB: Rivers\nC: Abuja\nD: Taraba\n")
    if questions.upper() == "C":
        print("Correct!")
        scores += 1
    else:
        print("Failed")

    questions = input("Question 6:\nThe national anthem of Nigeria has been 'Arise  O Compatriots' since 1978."
                      "What was the previous national anthem?\nA: Nigeria We Hail Thee\nB: O' God of Creation\n"
                      "C: Oh, say can you see\nD: O'er the land of the free\n")
    if questions.upper() == "A":
        print("Correct!")
        scores += 1
    else:
        print("Failed")

    questions = input("Question 7:\nWhat is the capital of Kwara State?\nA: Ilorin\nB: Omu-Aran\nC: Offa\n"
                      "D: Okanle\n")
    if questions.upper() == "A":
        print("Correct")
        scores += 1
    else:
        print("Failed")

    questions = input("Question 8:\nWho was the first senate president of the fourth republic?\nA: Ken Nnamani\n"
                      "B: David Mark\nC: Ahmed Lawan\nD: Evan Enwerem\n")
    if questions.upper() == "D":
        print("Correct")
        scores += 1
    else:
        print("Failed")

    questions = input("Question 9:\nWhat was General Babangida's position before becoming president?"
                      "\nA: Chief of Army Staff\nB: Minister\nC: Senator\nD: Prisoner\n")
    if questions.upper() == "A":
        print("Correct!")
        scores += 1
    else:
        print("Failed")

    questions = input("Question 10:\nNigeria is divided into 36 states. Which one is the largest by area?\n"
                      "A: Lagos\nB: Kano\nC: Niger State\nD: Abuja\n")
    if questions.upper() == "C":
        print("Correct!")
        scores += 1
    else:
        print("Failed")

    questions = input("Question 11:\nNigeria adopted what currency in 1973? Nigeria still uses this currency.\n"
                      "A: Pounds\nB: Kobo\nC: Naira\nD: Mint\n")
    if questions.upper() == "C":
        print("Correct!")
        scores += 1
    else:
        print("Failed")

    questions = input("Question 12:\nWhose face is on the 20 Naira Note?\nA: Murtala Muhammed\nB: Ladi Kwali\n"
                      "C: Mallam Alijy Mai-Bornu\nD: Nnamdi Azikiwe\n")
    if questions.upper() == "A":
        print("Correct!")
        scores += 1
    else:
        print("Failed")

    questions = input("Question 13:\nNigeria's flag consists of two colors. What are they?\nA: Green and green\n"
                      "B: White and green\nC: Yellow and white\nD: White and blue\n")
    if questions.upper() == "B":
        print("Correct!")
        scores += 1
    else:
        print("Failed")

    questions = input("Question 14:\nThe name of which city of Nigeria translates to 'by the edge of the meadow' "
                      "in Yoruba?\nA: Osun\nB: Ibadan\nC: Oyo\nD: Kwara\n")
    if questions.upper() == "B":
        print("Correct!")
        scores += 1
    else:
        print("Failed")

    questions = input("Question 15:\nWhat is the capital of Abia state?\nA: Amaeke\nB: Aba\nC: Ohafia\n"
                      "D: Umuahia\n")
    if questions.upper() == "D":
        print("Correct!")
        scores += 1
    else:
        print("Failed")

    questions = input("Question 16:\nNigerians Wole Soyinka, Ben Okri and Chinua Achebe have all achieved renown "
                      "in which field?\nA: Poetry\nB: Literature\nC: English\nD: Story telling\n")
    if questions.upper() == "B":
        print("Correct!")
        scores += 1
    else:
        print("Failed")

    questions = input("Question 17:\nKnown for having features that appear like a human face, Zuma Rock is "
                      "situated near what Nigerian city?\nA: Abeokuta\nB: Niger\nC: Abuja\nD: Port-Harcourt\n")
    if questions.upper() == "C":
        print("Correct!")
        scores += 1
    else:
        print("Failed")

    questions = input("Question 18:\nIn 1967 Nigeria suffered from a civil war when the south-east part of "
                      "the country broke away to set up a separate state under which name?\nA: Militants\n"
                      "B: Biafra\nC: Amotekun\nD: Vigilante\n")
    if questions.upper() == "B":
        print("Correct!")
        scores += 1
    else:
        print("Failed")

    questions = input("Question 19:\nWhich world-famous Nigerian novelist was the author of 'Things Fall Apart',"
                      "a book which commemorates the greatness of Igbo society and\nthe challenges which white "
                      "men have brought to it?\nA: Wole Soyinka\nB: Ben Okri\nC: Chinua Achebe\n"
                      "D: Christopher Okigbo\n")
    if questions.upper() == "C":
        print("Correct!")
        scores += 1
    else:
        print("Failed")

    questions = input("Question 20:\nWho was Olusegun Obasanjo's Vice President during his first term as"
                      "elected president?\nA: Peter Obi\nB: Shehu Shagari\nC: Abubakar Atiku\n"
                      "D: Nasiru Elrufai\n")
    if questions.upper() == "C":
        print("Correct!")
        scores += 1
    else:
        print("Failed")

    print("You got " + str(scores) + " questions correct!!!")


quiz_game()


def play_again():
    response = input("Do you want to play again? (yes or no) : ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


while play_again():
    quiz_game()


print("Thank you for taking the quiz")