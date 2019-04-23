person = {'name':'Jack', 'age': 26, 'salary': 4534.2}
print(person['age']) # Output: 26

person['salary'] = 100000000000000000000000
print(person)

del person['age']
print(person)
