import random

def hangman():
    words = ["python", "java", "javascript", "php", "kod", "kot", "pies", "lis"]
    random_index = random.randint(0, len(words)-1)
    word = words[random_index]
    stages = ["",
             "________   ",
             "|      |   ",
             "|      |   ",
             "|      0   ",
             "|     /|\  ",
             "|     / \  ",
             "|          "
            ]
    letters = list(word)
    board = ["_"] * len(word)
    win = False
    wrong = 0

    print("Gra w Wisielca")
    print("\n")
    print(" ".join(board))

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Odgadnij literę: "
        char = input(msg)

        if char in letters:
            char_index = letters.index(char)
            board[char_index] = char
            letters[char_index] = '$'
        else:
            wrong += 1

        print(" ".join(board))
        print("\n".join(stages[0:wrong+1]))

        if "_" not in board:
            print("\n")
            print("Wygrałeś!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages))
        print("\n Przegrałeś! Miałeś odgadnąć: {}.".format(word))




hangman()