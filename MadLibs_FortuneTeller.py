# Author: Stephen Tang
# Date: 12/1/2021
# Description: This program is a 2 player game. As the program runs, one player will ask a series of questions for the
# second player to answer while the first player inputs those responses to the appropriate questions. The final output
# will be displayed at the end of the game with an option to quit or to keep playing.

while True:
    print('''
        Welcome to the MadLibs Fortune Teller!
        Player 1 please ask Player 2 a Yes or No question
        ''')
    yes_no = input("Are you finished asking a Yes or No question? Enter 'Y' if Yes or 'N' if No: ").upper()
    if yes_no == "N":
        pass
    elif yes_no == "Y":
        color = input("Player 1 please ask Player 2 to choose a color - purple, blue, red or green: ").lower()
        if color == "purple":
            chosen_num = int(input("Player 1 please ask Player 2 to choose either 1 or 3: "))
            if chosen_num == 1:
                answer = input("Player 1 please ask Player 2 to choose an adjective: ")
                print("Signs point to a very", answer + " yes.")
                play_again = input("Would you like to play again? Enter 'Y' if Yes or 'N' if No: ").upper()
                if play_again == "N":
                    print("Thank you for playing MadLibs Fortune Teller!")
                    break
            elif chosen_num == 3:
                answer = input("Player 1 please ask Player 2 to choose a person's name in the room: ")
                print("Don't believe anything", answer + " says.")
                play_again = input("Would you like to play again? Enter 'Y' if Yes or 'N' if No: ").upper()
                if play_again == "N":
                    print("Thank you for playing MadLibs Fortune Teller!")
                    break
        if color == "blue":
            chosen_num = int(input("Player 1 please ask Player 2 to choose either 7 or 8: "))
            if chosen_num == 7:
                answer1 = input("Player 1 please ask Player 2 to choose a number greater than 1: ")
                answer2 = input("Player 1 please ask Player 2 to choose a plural noun: ")
                print("I see", answer1 + " big", answer2 + " in your future.")
                play_again = input("Would you like to play again? Enter 'Y' if Yes or 'N' if No: ").upper()
                if play_again == "N":
                    print("Thank you for playing MadLibs Fortune Teller!")
                    break
            if chosen_num == 8:
                answer = input("Player 1 please ask Player 2 to choose an adjective: ")
                print("The skies are", answer + ". The future is uncertain.")
                play_again = input("Would you like to play again? Enter 'Y' if Yes or 'N' if No: ").upper()
                if play_again == "N":
                    print("Thank you for playing MadLibs Fortune Teller!")
                    break
        if color == "red":
            chosen_num = int(input("Player 1 please ask Player 2 to choose either 5 or 6: "))
            if chosen_num == 5:
                answer1 = input("Player 1 please ask Player 2 to choose an adjective: ")
                answer2 = input("Player 1 please ask Player 2 to choose a singular noun: ")
                print("Picture a/an", answer1, answer2 + ". That is your answer.")
                play_again = input("Would you like to play again? Enter 'Y' if Yes or 'N' if No: ").upper()
                if play_again == "N":
                    print("Thank you for playing MadLibs Fortune Teller!")
                    break
            if chosen_num == 6:
                answer = input("Player 1 please ask Player 2 to choose an article of clothing that you are wearing: ")
                print("You will find the answer in your", answer + ".")
                play_again = input("Would you like to play again? Enter 'Y' if Yes or 'N' if No: ").upper()
                if play_again == "N":
                    print("Thank you for playing MadLibs Fortune Teller!")
                    break
        if color == "green":
            chosen_num = int(input("Player 1 please ask Player 2 to choose either 2 or 4: "))
            if chosen_num == 2:
                answer = input("Player 1 please ask Player 2 to choose an adjective: ")
                print("Signs point to a very", answer + " no.")
                play_again = input("Would you like to play again? Enter 'Y' if Yes or 'N' if No: ").upper()
                if play_again == "N":
                    print("Thank you for playing MadLibs Fortune Teller!")
                    break
            if chosen_num == 4:
                answer = input("Player 1 please ask Player 2 to choose a part of the body: ")
                print("What does your", answer + " tell you?")
                play_again = input("Would you like to play again? Enter 'Y' if Yes or 'N' if No: ").upper()
                if play_again == "N":
                    print("Thank you for playing MadLibs Fortune Teller!")
                    break
