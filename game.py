##importing phrase.py for testing
from phrase import Phrase
import random
import os


class Game:
    phrase_one = Phrase("If money doesn't grow on trees, why do bankes have branches?")
    phrase_two = Phrase("Life is a bowl of soup, and I'm a fork.")
    phrase_three = Phrase("Your wife is a whore")
    phrase_four = Phrase("Sure, I can help you out. Which way did you come in?")
    phrase_five = Phrase("See you in the zombie apocalypse.")
    def __init__(self, missed = 0):
        self.missed = missed
        self.phrases = [self.phrase_one, self.phrase_two, self.phrase_three, self.phrase_four, self.phrase_five]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]
    
    def create_phrases(self):
        with open('phrases.txt', 'r') as file:
            self.bunch_of_phrases = [line.strip() for line in file]
            
        
    def start(self):
        self.welcome()
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) is False:
            print("\nNumber missed: {}\n".format(self.missed))
            self.active_phrase.display(self.guesses)
            try:
               user_guess = self.get_guess()
               if not user_guess.isalpha():
                   print("\nThat is not a letter!")
                   continue
            except:
               print("\nThere was an error with your input. Please try again.")
               continue   
            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
               self.missed += 1
        self.game_over()
             
    def get_random_phrase(self):
        ran_phrase = random.choice(self.phrases)
        return ran_phrase
    
    def welcome(self):
        print("*******************************************\n")
        print("   Hello! Welcome to the PHRASE HUNTING\n")
        print("*******************************************")
    def get_guess(self):
        guess = input("\n\nEnter a guess  ")
        return guess
    
    def game_over(self):
        if self.missed == 5:
            print("*************************************")
            print("          Sorry! You lost!")
            print("*************************************")
        else:
            print("*************************************")
            print("      Congratulations! You Won!")
            print("*************************************")


        
            