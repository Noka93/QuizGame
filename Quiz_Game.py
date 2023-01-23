# Prompt the user to enter a name
# Prompt the user to select an input to proceed with the quiz
# Using the selection statement, ask the user questions and then print result if user input is correct or false

name = input("Enter your name\n")

print(f"Welcome {name} to your quiz game")

start_game = input("Enter 1 to start : ")


def new_quiz():
    guesses = []
    correct_scores = 0
    question_number = 1

    for count in quiz_questions:
        print()
        print(count)
        for counter in options[question_number - 1]:
            print(counter)
        guess = input("Enter a correct answer: ")

        guess = guess.upper()

        guesses.append(guess)

        correct_scores += quiz_answers(quiz_questions.get(count), guess)

        question_num += 1

    display_score(correct_scores, guesses)


def quiz_answers(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Failed")
        return 0


def display_score(correct_scores, guesses):
    print("Result")
    print()
    print("Answers: ", end=" ")
    for counter in quiz_questions:
        print(quiz_questions.get(counter), end=" ")
    print()

    print("Guesses: ", end=" ")
    for counter in guesses:
        print(counter, end=" ")
    print()

    print()

    scores = (correct_scores / len(quiz_questions) * 100)
    print("Your score is: " + str(scores) + "%")


def play_again():
    response = input("Do you want to play again? (yes or no) : ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


quiz_questions = {
    "Question 1:\nWhen did Nigeria get her Independence?": "D",
    "Question 2:\nWhat does BBC  stand for?": "C",
    "Question 3:\nHow many days are in a leap year?": "C",
    "Question 4:\nIn meters, how long is an Olympic swimming pool?": "A",
    "Question 5:\nWhat is the capital of Nigeria?": "C",
    "Question 6:\nThe national anthem of Nigeria has been Arise  O Compatriots since 1978. What was the "
    "previous national anthem?": "A",
    "Question 7:\nWhat is the capital of Kwara State?": "A",
    "Question 8:\nWho was the first senate president of the fourth republic?": "D",
    "Question 9:\nWhat was General Babangida's position before becoming president?": "A",
    "Question 10:\nNigeria is divided into 36 states. Which one is the largest by area?": "C",
    "Question 11:\nNigeria adopted what currency in 1973? Nigeria still uses this currency.": "C",
    "Question 12\nWhose face is on the 20 Naira Note?": "A",
    "Question 13\nNigeria's flag consists of two colors. What are they?": "B",
    "Question 14:\nThe name of which city of Nigeria translates to 'by the edge of the meadow' in Yoruba?":
        "B",
    "Question 15:\nWhat is the capital of Abia state?": "D",
    "Question 16:\nNigerians Wole Soyinka, Ben Okri and Chinua Achebe have all achieved renown in which field?":
        "A",
    "Question 17:\nKnown for having features that appear like a human face, Zuma Rock is situated near what "
    "Nigerian city?": "C",
    "Question 18:\nIn 1967 Nigeria suffered from a civil war when the south-east part of the country broke away "
    "to set up a separate state under which name?": "B",
    "Question 19:\nWhich world-famous Nigerian novelist was the author of 'Things Fall Apart', a book which "
    "commemorates the greatness of Igbo society and the challenges which white men have brought to it?":
        "C",
    "Question 20:\nWho was Olusegun Obasanjo's Vice President during his first term as elected president?":
        "C"
}

options = [["A: 1994", "B: 1963", "C: 1988", "D: 1960"],
           ["A: Battery Backed Cache", "B: Broadband Conducted ", "C: British Broadcasting Corporation",
            "D: Broadband Content"],
           ["A: 365", "B: 266", "C: 366", "D: 401"],
           ["A: 50 Meters", "B: 500 Meters", "C: 100 Meters", "D: 150 Meters"],
           ["A: Lagos", "B: Rivers", "C: Abuja", "D: Taraba"],
           ["A: Nigeria We Hail Thee", "B: O' God of Creation", "C: Oh, say can you see",
            "D: O'er the land of the free"],
           ["A: Ilorin", "B: Omu-Aran", "C: Offa", "D: Okanle"],
           ["A: Ken Nnamani", "B: David Mark", "C: Ahmed Lawan", "D: Evan Enwerem"],
           ["A: Chief of Army Staff", "B: Minister", "C: Senator", "D: Prisoner"],
           ["A: Lagos", "B: Kano", "C: Niger State", "D: Abuja"],
           ["A: Pounds", "B: Kobo", "C: Naira", "D: Mint"],
           ["A: Murtala Muhammed", "B: Ladi Kwali", "C: Mallam Alijy Mai-Bornu", "D: Nnamdi Azikiwe"],
           ["A: Green and green", "B: White and green", "C: Yellow and white", "D: White and blue"],
           ["A: Osun", "B: Ibadan", "C: Oyo", "D: Kwara"],
           ["A: Amaeke", "B: Aba", "C: Ohafia", "D: Umuahia"],
           ["A: Poetry", "B: Literature", "C: English", "D: Story telling"],
           ["A: Abeokuta", "B: Niger", "C: Abuja", "D: Port-Harcourt"],
           ["A: Militants", "B: Biafra", "C: Amotekun", "D: Vigilante"],
           ["A: Wole Soyinka", "B: Ben Okri", "C: Chinua Achebe", "D: Christopher Okigbo"],
           ["A: Peter Obi", "B: Shehu Shagari", "C: Abubakar Atiku", "D: Nasiru Elrufai"]
           ]


new_quiz()

while play_again():
    new_quiz()

print("Thank you for playing with us")
