import random

print('Let\'s play hangman')
#list of words that could randomly be selected
word_bank = ('desk', 'phone', 'harpie', 'microphone', 'kazoomaniafool', 'football')

#wrote this alphabet list to pop off letters guessed so I could tell them if they have already guessed it.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

guessed_letters = []

#function to select the hangman word from the word_bank
def bank():
  chosen_word = random.choice(word_bank)
  return chosen_word

word = bank()

#counter to decrement which each wrong choice.  Not implemented yet.
count = 10
#word_length = len(word())
dash_word = ['_ '] * len(word)

def display_word():
  display = " "
  for letter in word:
    if guessed_letters.count(letter):
      display += letter + " "
    else:
      display += "_ "
  print(display)
  print()
  

def guessed(letter):
  if letter in guessed_letters:
    print('You have already guessed this letter')
    exit
  else:
    guessed_letters.append(letter)

#function to check if the letter guessed was in the word and replace the dash with it. The check to see if it is in the word works
def check_letter(letter):
  if letter in word:
    print(f'You guessed one, {letter} is in the word.')
  else:
    nonlocal count -=1
    print(f'Nope! {letter} is not in this word. You have {counter} guesses left')
    
 

#creates the dashes with the length of the word


#main loop to play game. work in progress
letter = ''
while letter != "exit":
  display_word()
  print('Guess all the correct letters to win? You will be allowed 10 wrong choices before you lose the game')
  letter = input("Choose a letter: ")
  guessed(letter)
  print('These are your guessed letters ' + str(guessed_letters))
  #print('You have ' + str(counter) + ' guesses left.')
  check_letter(letter)

