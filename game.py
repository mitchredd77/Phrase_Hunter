##importing phrase.py for testing
from phrase import Phrase
import random
import os


class Game:

    def __init__(self, missed = 0):
        self.missed = missed
        self.phrases = []
        self.guesses = [" "]
        self.on_switch = True

## Pulls the phrases from a txt file and randonly choose 5 to put in the phrases list 
    def create_phrases(self):
        with open('phrases.txt', 'r') as file:
            self.bunch_of_phrases = [line.strip() for line in file]
        self.phrases = random.sample(self.bunch_of_phrases, 5)
            
  ## The guts of the program       
    def start(self):
        self.welcome()
        self.create_phrases()
        self.active_phrase = Phrase(self.get_random_phrase())
        while self.on_switch is True:
            print("\nNumber missed: {}\n".format(self.missed))
            self.active_phrase.display(self.guesses)
            try:
               user_guess = self.get_guess()
               if len(user_guess) > 1:
                   print("\nPlease only one letter!")
                   continue
               if not user_guess.isalpha():
                   print("\nThat is not a letter!")
                   continue
            except:
               print("\nThere was an error with your input. Please try again.")
               continue   
            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
               self.missed += 1
               if self.missed == 5:
                   self.game_over()
                   self.on_switch = False   
            self.check_end()
            
## Check if the person has won after they input a guess and asks if they want to play again
    def check_end(self):
        if self.active_phrase.check_complete(self.guesses) == True:
             self.active_phrase.display(self.guesses)
             print("\n\n**********************************************************")
             print("\nCORRECT PHRASE! TOTAL MISSES: {}".format(self.missed))
             print("\n**********************************************************")
             play_again = input("\nWould you like to play again?(Y or N)  ")
             
             if play_again == "Y" or play_again == "y":
                  self.missed = 0
                  self.guesses = [" "]
                  self.create_phrases()
                  self.active_phrase = Phrase(random.choice(self.phrases))
             else:
                  self.on_switch = False
                  
 ###  Pulls a phrase randomly from the phrases list           
    def get_random_phrase(self):
        ran_phrase = random.choice(self.phrases)
        return ran_phrase
    
    
    def welcome(self):
        print("*******************************************\n")
        print("   Hello! Welcome to PHRASE HUNTING\n")
        print("*******************************************")

##  Prompt for a guess by the player
    def get_guess(self):
        guess = input("\n\nEnter a guess  ")
        return guess
    
 ## Displays when the player has tried 5 times unsuccessfully and the game is over       
    def game_over(self):
        if self.missed == 5:
            print("*************************************")
            print("          Sorry! You lost!")
            print("*************************************")
        
            


        
            