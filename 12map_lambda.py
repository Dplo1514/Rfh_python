people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]
def check_adult(person):
    return ("성인" if person['age'] > 20 else '청소년')

result = map(check_adult , people)
result = map(lambda x:x , people) #/lambda

print(list(result))