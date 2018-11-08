d = {}
num = int(input())

for i in range(num):
    user_input = input('')
    name, number = user_input.split(' ')
    d[name] = number

for i in range(num):
    user_input = input('')
    if user_input in d:
        print(str(user_input), '=', int(d[user_input]), sep='')
    else:
        print('Not found')
