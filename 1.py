import random 
turns = ['rock', 'paper', 'scissors']

human_turn = input('Ievadi savu gājienu:')
computer_turn = random.choice(turns)

def play():
    human_turn = input('Ievadi savu gājienu:')
    computer_turn = random.choice(turns)   
     
    if human_turn == computer_turn:
        print('Neizšķirts!')
    elif human_turn == 'rock' and computer_turn == 'scissors':
        print('Tu uzvari!')
    elif human_turn == 'paper' and computer_turn == 'rock':
        print('Tu uzvari!')
    elif human_turn == 'scissors' and computer_turn == 'paper':
        print('Tu uzvari!')
    else:
        print('Dators uzvar, TU zaudē!')

while True:
    answer = input("Velreiz?")
    if answer == 'Ja':
        play()
    elif answer == 'Ne':
        break
    else:
        print("Nesaprotu")
