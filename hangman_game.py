# Hangman game

from random import choice

words = ['lockdown', 'wisdom', 'calligraphy', 'attraction', 'visionary', 'abruptly', 'awkward',
         'vocabulary', 'unknown', 'injury', 'galaxy', 'microwave', 'keyboard,' 'research', 'Wednesday',
         'industry', 'baldness', 'hungry', 'elephant', 'translate', 'trustworthy', 'brazilian', 'mythology',
         'courage', 'September', 'January', 'empire', 'rocket', 'society', 'friendship']

ramdom_word = list(choice(words).upper())

def hangman_game(right_guess):  
    for g in ramdom_word:
       if g in right_guess:
           print(g, end= '')
       else:
           print('_ ', end= '')

right_guess = []
wrong_guess = []

print("\n--- WELCOME TO THE HANGMAN GAME ---\n\nYou can make 6 mistakes. GOOD LUCK!\n")
for i in ramdom_word:
    print('_ ', end='')
    
x = 6 
while x > 0:
    letter = input('\n\nType a letter or guess the word: ').upper()
    if set(list(letter)).issuperset(ramdom_word):
        x = 0
        word_random = ''.join(ramdom_word)
        print(word_random)
        print('--- Game over. YOU WON! ---')
        break
    if (letter in right_guess) or (letter in wrong_guess) :
        guess_repeated = input('\nYou already guessed that. Press enter to make another guess.')
        print()
        hangman_game(right_guess)
    elif letter in ramdom_word:
        right_guess.append(letter)
        print()
        hangman_game(right_guess)
        #print(f'\n{right_guess}')
        if set(right_guess).issuperset(ramdom_word):
                x = 0
                print('\n--- Game over. YOU WON! ---')
    else:
        wrong_guess.append(letter)
        x -= 1
        print(f'\nWrong guess. You can make {x} mistake(s)')
        print()
        hangman_game(right_guess)
        if x == 0:
            print('\n--- Game over. YOU LOST. ---')
