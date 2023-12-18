#Strip()
#
# with open('data/chicken.txt', 'r') as f:
#     for line in f:
#         print(line.strip())

#splite() -> 사용해서 list를 만들면 값이 str 값으로 설정이 되기 때문에 상황에 맞게 형변환 필요.
# my_str = 'Kim, Yuna'
# print(my_str.split(', '))

# with open('data/chicken.txt' ,'r') as f:
#     total = 0
#     days = 0
#     for line in f:
#         data = line.strip().split(': ')
#         revenue = data[1]
#         total += int(data[1])
#         days += 1
#     average = total / days
#
#     print(average)

with open('new_file.txt', 'a') as f:
    f.write('hello world!\n')
    f.write('my name is ryan')
