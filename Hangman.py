import random

name_of_game = ['H', 'A', 'N', 'G', 'M', 'A', 'N']
list_of_words = ['python', 'java', 'swift', 'javascript']
computer_choice = random.choice(list_of_words)


def hint(choice):
    i = 0
    while i != len(choice):
        print('-', end="")
        i += 1


for i in name_of_game[:-1]:
    print(i, end='')
print(name_of_game[-1])
print()
hint(computer_choice)
print()
i = 0
known_letters = ['-'] * len(computer_choice)
named_letters = []
f = False
while i != 8:
    print('Input a letter:', end='')
    letter = input()
    if letter in named_letters:
        if letter in known_letters:
            print('No improvements.\n')
        else:
            print("That letter doesn't appear in the word.\n")
        print()
        print(''.join(known_letters))
    else:
        if letter in computer_choice:
            for j in range(len(computer_choice)):
                if letter == computer_choice[j]:
                    known_letters[j] = letter
        else:
            print("That letter doesn't appear in the word.")
        print()
        print(''.join(known_letters))
    i += 1
    named_letters.append(letter)
    if '-' not in known_letters:
        print('You guessed the word!')
        print('You survived!')
        f = True
        break
if not f:
    print('You lost!')
