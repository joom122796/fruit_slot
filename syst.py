from random import randint
from fruits import fruits
balance = 100

def rolling():
  global balance
  balance = balance - 20
  slot = fruits[randint(0,5)]
  slot2 = fruits[randint(0,5)]
  slot3 = fruits[randint(0,5)]
  print(slot)
  print(slot2)
  print(slot3)
  if balance <= 0:
    quit()
  else:
    if slot == slot2:
      if slot == slot2 and slot == slot3:
        if slot == fruits[5]:
          balance = 0
        elif slot == fruits[1]:
          balance = balance + 500
          print(f'Congratulations! Your new balance is: £{balance}')
        else:
          balance = balance + 100
          print(f'Congratulations! Your new balance is: £{balance}')
      else:
        if slot == fruits[5]:
          balance = balance - 100
          print(f'You hit two skulls! Your new balance is: £{balance}')
        else:
          balance = balance + 50
          print(f'Congratulations! Your new balance is: £{balance}')
    elif slot == slot3:
      if slot == fruits[5]:
        balance = balance - 100
      else:
        balance = balance + 50
        print(f'Congratulations! Your new balance is: £{balance}')
    elif slot2 == slot3:
      if slot2 == fruits[5]:
        balance = balance - 100
      else:
        balance = balance + 50
        print(f'Congratulations! Your new balance is: £{balance}')
  if balance <= 0:
    print('You are out of luck (and money)! You can no longer use the slot machine')
    quit()
  else:
    cont = int(input(f'You current have £{balance} in total earnings. Would you like to quit with the earnings or continue playing? \nEnter 1 to continue and 2 to quit. \nChoice: '))
    while cont != 1 and cont != 3:
      cont = int(input('Invalid option. \nEnter 1 to continue and 2 to quit. \nChoice: '))
    else:
      if cont == 1:
        rolling()
      else:
        quit()
