import random

with open('vocabulary.txt', 'r') as f:
    voca = {}
    for line in f:
        data = line.strip().split(': ')
        english_word, korea_word = data[0], data[1]
        voca[english_word] = korea_word

keys = list(voca.keys())

while True:
    index = random.randint(0, len(keys) - 1)
    english_word = keys[index]
    korea_word = voca[english_word]

    input_answer = input('{}: '.format(korea_word))
    if input_answer == 'q':
        break

    if english_word == input_answer:
        print('맞았습니다!\n')
    else:
        print('아쉽습니다. 정답은 {}입니다.\n'.format(english_word))


# with open('vocabulary.txt', 'w') as f:
#     while True:
#         english_word = input('영어 단어를 입력하세요: ')
#         if english_word == 'q':
#             break
#         korea_word = input('한국어 뜻을 입력하세요: ')
#         if korea_word == 'q':
#             break
#
#         f.write('{}: {}\n'.format(english_word, korea_word))

# with open('vocabulary.txt', 'r') as f:
#     for line in f:
#         data = line.strip('\n').split(': ')
#
#         question = data[1]
#         answer = data[0]
#
#         input_answer = input('{}: '.format(question))
#         if answer == input_answer:
#             print('맞았습니다!\n')
#         else:
#             print('아쉽습니다. 정답은 {}입니다.\n'.format(answer))

