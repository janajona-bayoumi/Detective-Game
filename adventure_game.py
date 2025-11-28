import time
import random


def print_pause(message, pause_time=2):
    """
    Print a message and pause for a specified amount of time.

    Args:
        message (str): The message to be printed.
        pause_time (int, optional): Pause time in 2 seconds.
    """
    print(message)
    time.sleep(pause_time)  # For pausing between lines


def add_clue_to_inventory(clue_name, user_score):
    """
    Add a clue to the user's inventory based on their choice.

    Args:
        clue_name (str): The name of the clue to add.
        user_score (int): The current score of the user.

    Returns:
        int: Updated user score after adding the clue.
    """
    print(f"Add {clue_name} to your inventory as a clue?")
    while True:
        clue_choice = input("> ").lower().strip()
        if clue_choice == "yes":
            print("100 points have been added to your score!")
            user_score += 100
            print("---------------")
            break
        elif clue_choice == "no":
            print("---------------")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    return user_score


def investigate_location(location, clues):
    """
    Investigate a specific location in the game.

    Args:
        location (str): The location to investigate.
        clues (str): Description of clues found at the location.
    """
    print_pause(f"You go to the {location}")
    print_pause(f"You look around the {location}, {clues}")
    print_pause("You look around one more time to make sure that you're done")
    print_pause(f"In the corner of the {location}, you find a clue")


def question_suspects(suspects, suspect_questions, suspect_answers):
    """
    Question suspects in the game.

    Args:
        suspects (list): List of suspects' names.
        suspect_questions (dict): Dictionary mapping suspects' questions.
        suspect_answers (dict): Dictionary mapping suspects to their answers.
    """
    random.shuffle(suspects)
    for suspect in suspects:
        print_pause(f"You question {suspect}")
        print_pause(f"You: {suspect_questions[suspect]}")
        print_pause(f"{suspect}: {suspect_answers[suspect]}")
        print("---------------")


def play_detective_game():
    """Play the detective game."""
    print_pause("Oh no! The mayor of the town has been murdered!")
    print_pause("It's up to you detective to find out who the murderer is!")
    print_pause("Are you ready detective?")
    start_choice = input("> ").lower().strip()

    if start_choice == "yes":  # Starting game
        user_score = 0

        investigate_location("bedroom", "the walls were covered in blood")
        user_score = add_clue_to_inventory("knife", user_score)

        investigate_location("kitchen", "the kitchen was neat")
        user_score = add_clue_to_inventory("glasses", user_score)

        investigate_location("living room", "you find a wedding ring")
        user_score = add_clue_to_inventory("wedding ring", user_score)

        print_pause("You leave the mayor's house and go to your office")
        print_pause("You open your files, you have 3 suspects")
        print_pause("1- Mayor's former assistant, Elliot Ward, 54")
        print_pause("2- Mayor's wife, Andie Bell, 55")
        print_pause("3- Mayor's only son, Sal Singh, 23")
        print_pause("You decide to question them the next day")
        print_pause("------------------", 3)

        suspects = ['Elliot Ward', 'Andie Bell', 'Sal Singh']
        suspect_questions = {
            'Elliot Ward': "Did you have an argument with the mayor?",
            'Andie Bell': "How was the mayor like the day before his murder?",
            'Sal Singh': "How was your relationship with the mayor?"
        }  # Questions for each suspect

        suspect_answers = {
            'Elliot Ward': "He thought I was trying to steal from citizens"
            "after I suggested to increase the taxes to double!"
            "I only wanted what was best for him!",
            'Andie Bell': "He was too quiet that night,"
            "usually he would tell me about what happened during his day,"
            "but when I tried to ask him what's wrong he shouted loudly at me!"
            "He never shouted at me so I ignored him the whole night!",
            'Sal Singh': "Me and my father weren't on the best terms."
            "I have no reason to kill him! It's not like I'll take his wealth."
        }  # Answers of the previous questions

        question_suspects(suspects, suspect_questions, suspect_answers)

        print_pause("Investigation completed!")
        print_pause(f"Your score: {user_score}")

        # Accusing suspects depending on score
        if user_score >= 300:
            print_pause(f"Based on the score {user_score}, you accuse Elliot!")
            print_pause("After asking, you find that Elliot wears glasses,")
            print_pause("which were similar to the ones you found")
            print_pause("When you went to his house, he wasn't wearing them!")
            print_pause("When you asked him about it, he dismissed it")
            print_pause("Saying it was unnecessary to ask this question")
            print_pause("Police arrested him, he admits killing the mayor!")
            print_pause("Congratulations! You identified the murderer!")
            print_pause("You have been given an award for your job!")
        elif user_score >= 200:
            print_pause(f"Based on your score {user_score}, you accuse Andie!")
            print_pause("After asking, you find Andie's ring was missing")
            print_pause("When asking her, she said it must've fallen.")
            print_pause("But you didn't believe her")
            print_pause("The police arrested her, and in the court,")
            print_pause("it was found out that Elliot is the murderer!")
            print_pause("Sadly, you lost your job as a detective!")
        else:
            print_pause(f"Based on your score {user_score}, you accuse Sal!")
            print_pause("After asking, Sal waas nervous and shaky alibi.")
            print_pause("The police arrested him, and in the court,")
            print_pause("it was found out that Elliot is the murderer!")
            print_pause("Sadly, you lost your job as a detective!")

        print_pause("Play Again?")  # For replaying
        play_again = input("> ").lower().strip()
        if play_again == "yes":
            play_detective_game()
        else:
            print_pause("Thank you for playing!")

    else:
        print_pause("Invalid input, please try again")


play_detective_game()
