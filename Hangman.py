import random
list_of_words = ["mama", "dada", "papa", "nana", "bhau"]
comp_guess = random.choice(list_of_words)
print(f"Computer's guess: {comp_guess}")

blank_spaces = len(comp_guess) * "_"
print(f"Guess the word: {blank_spaces}")

available_guesses = 6

while available_guesses > 0:
    my_guess = input("Enter your guess: ").lower()
    position =""
    for i in comp_guess:
        if my_guess == i:
            position+=i
        else:
            position+="_"
    
print(position)
        





available_guesses = 6



