import random

rounds = 5
score = 0

while rounds > 0:
    randNum1 = random.choice(range(1, 11))
    randNum2 = random.choice(range(1, 11))
    randop = random.choice(['+', '-', 'x', '÷'])
    answ = float(input('What is {} {} {} \n'.format(randNum1, randop, randNum2)))

    if randop == '+':
        if answ == randNum1 + randNum2:
            print('Correct!')
            score += 1
        else:
            print('Incorrect!')
    if randop == '-':
        if answ == randNum1 - randNum2:
            print('Correct!')
            score += 1
        else:
            print('Incorrect!')
    if randop == 'x':
        if answ == randNum1 * randNum2:
            print('Correct!')
            score += 1
        else:
            print('Incorrect!')
    if randop == '÷':
        if answ == randNum1 / randNum2:
            print('Correct!')
            score += 1
        else:
            print('Incorrect!')
        
    rounds -= 1

print(f"Your score is {score} out of 5.")

