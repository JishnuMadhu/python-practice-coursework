import random

list1 = ['stone','paper','scissor']
comp = random.choice(list1)
player = input('enter your choice')
print(f'computer: {comp} \nPlayer: {player}')
if comp == player:
    print('it is a tie!!!!!!!')
elif comp == 'stone':
    if player == 'paper':
        print('paper cover stone , player win')
    else:
        print('stone beat scissor, computer win')
elif comp == 'scissor':
    if player == 'paper':
        print('scissor cut paper, computer win')
    else:
        print('stone beat scissor, player win')
elif comp == 'paper':
    if player == 'scissor':
        print('scissor cut paper, player win')
    else:
        print('paper covers stone, computer win')