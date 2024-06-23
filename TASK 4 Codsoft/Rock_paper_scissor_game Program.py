import random
userscore = 0
compscore = 0

while True:
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid Input. Enter a valid input: ").lower()
    valid_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(valid_choices)
    
    winner = ''
    if choice == computer_choice:
        winner = 'tie'
    elif (choice == 'rock' and computer_choice == 'scissors') or (choice == 'scissors' and computer_choice == 'paper') or (choice == 'paper' and computer_choice == 'rock'):
        winner = 'user'
        userscore+=1
    else:
        winner = 'computer'
        compscore+=1
        
    print("You chose: "+choice)
    print("Computer chose: "+computer_choice)
    if winner == 'tie':
        print("It is a tie")
    elif winner == 'user':
        print("You win")
    else:
        print("You lose")
    print("Score: User - "+str(userscore)+" , Computer - "+str(compscore))
    
    play_again = input("Do you want to play again (Type yes/no): ").lower()
    if play_again == 'no':
        print('Thank you fo playing')
        print('Final Score')
        print('User: '+str(userscore))
        print('Computer: '+str(compscore))
        break
    elif play_again != 'no' and play_again != 'yes':
        print('Invalid Choice')
        print('Final Score')
        print('User: '+str(userscore))
        print('Computer: '+str(compscore))
        break