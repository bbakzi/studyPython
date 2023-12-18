import random

ANSWER = random.randint(1,20)
NUM_TRIES = 4

guess = 0
tries = 0

while guess != ANSWER and tries < NUM_TRIES:
    guess = int(input('기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞춰 보세요: '.format(NUM_TRIES - tries)))
    tries += 1

    if ANSWER > guess:
        print('Up')
    elif ANSWER < guess:
        print('Down')

if guess == ANSWER:
    print('축하합니다. {}번 만에 숫자를 맞추셨습니다.'.format(tries))
else:
    print('아쉽습니다. 정답은 {}입니다.'.format(ANSWER))