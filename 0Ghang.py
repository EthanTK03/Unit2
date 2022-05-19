# Available files changed from original game

import random

play = True

while play == True:
    print("Files to choose from: america, s_america, mideast, states, africa, europe, asia \n")
    filename = input('What file would you like to use? ')
    f = open(filename + '.txt')

    text = []
    for line in f:
        if line.startswith('ran'):
            word = print(line[1:].strip())
        else:
            word = line
        text.append(word.strip().lower())

    ran = random.randrange(0,len(text))
    f.close()

    choices = []
    done = False
    turn = 5
    while done == False and turn>0: 
        done = True
        user_choice = input('Guess a letter: ')
        if user_choice not in text[ran]:
            turn = turn -1
        choices.append(user_choice)
        for c in text[ran]:
            if c in choices:
                print(c + ' ', end = '')
            else:
                print('_ ', end = '')

                done = False
        print('')
        print('\n'+ str(turn))
    print('\n Your word was ' + str(text[ran]) + '\n')

    replay = input('Play again? Type yes to replay: ')
    if replay == 'yes':
        print(' ')
        play = True
    else:
        play = False
        print('\n Thank you for playing')