import random

gretting = input('Are you ready to play rock paper scissor game with Mr-Computer (y/n) - ')
cho = ["r","p","s"]
count = 0
while gretting == 'y':
    num_win = 0
    num_tie = 0
    num_lose = 0
    num = int(input('inter the best out of num: '))
    while count < num:
        user_guess = input("To play this game choose from (r,p,s) r is for rock, p is for paper and s is for scissor - ")
        ran = random.choice(cho)
        if user_guess == ran :
            num_tie += 1
            print('you tied with Mr-Computer')
        if (user_guess == "p" and ran == "r") or (user_guess == "r" and ran == "s") or (user_guess == "s" and ran == "p") :
            num_win += 1
            print('congra you win!')
        if (user_guess == "r" and ran == "p") or (user_guess == "s" and ran == "r") or (user_guess == "p" and ran == "s") :
            num_lose += 1
            print('you lose!')
        count += 1

    if num_tie == num and (num_tie) == num_lose == num_win:
        print('you tied with mr-computer')
    if num_win > num_lose:
        print('congra YOU win the best out of three game aganist Mr-Computer', num_win, ' - ', num - num_win)
    else:
        print('you loose the overall match by', (num + num_tie) - num_win, ' -', num_win)

    rep = str(input('wanna play again (y/n): '))
    if rep == 'y':
        count = 0
        continue
    else:
        print('game over! tnx for playing')
        break

e = input('press any key to exit')

