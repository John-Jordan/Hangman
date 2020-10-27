import random
wrong_choices_allowed = 9
guessed_letters = []
word_bank = ('desk', 'phone', 'harpie', 'microphone', 'kazoomaniafool', 'football')

def bank():
  chosen_word = random.choice(word_bank)
  return chosen_word

word = bank()
def get_guesses_remaining():
  wrong_choices_allowed - len(set(guessed_letters) - set(word))

print('Let\'s play hangman')

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

def return_word():
  display = " "
  for letter in word:
    if guessed_letters.count(letter):
      display += letter + " "
    else:
      display += "_ "
  return display

  

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
    print(f'Nope! {letter} is not in this word.')


def get_guesses_remaining():
  return wrong_choices_allowed - len(guessed_letters)

def won():
  return return_word().replace(' ', '') == word

#main loop to play game. work in progress
letter = ''
while letter != "exit":
  return_word()
  display_word()
  print(f'Guess all the correct letters to win? You have {get_guesses_remaining()} guesses before you lose the game. Type exit to end game early.')
  letter = input("Choose a letter: ")
  guessed(letter)
  print('These are your guessed letters ' + str(guessed_letters))
  #print('You have ' + str(counter) + ' guesses left.')
  check_letter(letter) 
  if won():
    print('You won!')
  if get_guesses_remaining() > 0:
    continue

  if won():
    print('You won!')
  else:
    print(f'You lose! The word was {word}')
    exit

