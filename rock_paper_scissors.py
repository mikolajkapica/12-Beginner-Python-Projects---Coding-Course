import random

sequence = ['r', 'p', 's']
computer = random.choice(sequence)
user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")


while not user in sequence:
    print('Error. Write correctly your choice.') 
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    
        
    
def play():
    if user == computer:
        return 'It\'s a tie'

    elif is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's')  or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

def pick():
    if computer == 'r':
        return 'Computer chosed rock.'
    if computer == 'p':
        return 'Computer chosed paper.'
    if computer == 's':
        return 'Computer chosed scissors.'

print(play() + ' ' + pick())