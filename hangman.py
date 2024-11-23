import random

word_list = ["Apple", "Grapes", "Watermellon", "Banana"]
choose_word = random.choice(word_list).lower()

number_of_char = len(choose_word)

print(f"The game has selected a word from {word_list}, you have to guess a character of any one fruit")

display = []

for num in range(number_of_char):
    display += "_"

#print(display)

end_of_game = False
lives = 6

while not end_of_game:

    guess = input("guess a character between: ").lower()

    for position in range(number_of_char):
        letter = choose_word[position]
        if guess == letter:
            display[position] = letter
    if guess not in display:
        lives -= 1

    if not "_" in display:
        end_of_game = True
        print("you win")
    elif lives == 0:
        end_of_game = True
        print("you loose, no more lives left")

    print(display)



