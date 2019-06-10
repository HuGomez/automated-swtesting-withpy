my_set = {1, 2, 3}
my_dict = {'name': 'Jose', 'age': 39, 'grades': {2, 4, 5}}
another_dict = {1: 15, 2: 30, 3: 150}

lottery_player = {
    'name': 'Rolf',
    'numbers': (13, 45, 60, 22)
}

universities = [
    {
        'name': 'Oxford',
        'location': 'UK'
    },
    {
        'name': 'Harvard',
        'location': 'US'
    }
]

total = sum(lottery_player['numbers'])
print(total)
print('before ' + lottery_player['name'])
lottery_player['name'] = 'John'
print('after ' + lottery_player['name'])

student_list = [
    {
        'name': 'Godzi',
        'grades': (1, 2, 4)
    },
    {
        'name': 'Kraken',
        'grades': (1, 3, 5)
    },
    {
        'name': 'Kaiju',
        'grades': (5, 5, 5)
    },
]

total = 0
count = 0
for student in student_list:
    total += sum(student['grades'])
    count += len(student['grades'])


print(total/count)
