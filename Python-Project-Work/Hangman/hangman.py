#Guess the word or get hanged
import random
from hangman_art import stages,logo

from hangman_word import word_list
chosen_word = random.choice(word_list)
chosen_word = list(chosen_word)
end_of_game=False
word_length=len(chosen_word)
display=[]
lives=6
print(f"{logo}\n\n")
s=""
s=s.join(chosen_word)
for c in range(0, word_length):
    display+= "_"
   


while not end_of_game:
    char = input("Guess a letter:").lower()
   
    if char in display:
        print(f"You have already guessed {char}")

    for c in range(word_length):
            if(chosen_word[c] == char):
                display[c] = char
    
   
    print(f"".join(display))
    
    if char not in display:
        print(f"You guessed {char} wrong.That's not in the word.You lose live.")
        lives-=1
        if(lives==0):
            end_of_game = True
            print("YOU LOSE")
            print(f"Correct word was {s}")
        
    if "_" not in display:
        end_of_game=True
        print("YOU WIN")
    
    
    print(stages[lives])

