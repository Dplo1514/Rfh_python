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

for i , peoples in enumerate(people): #enumerate : 엘리먼트에 숫자를 붙혀줌
    name = peoples["name"]
    age = peoples["age"]
    print(i , name , age)
    if i > 3 :
        break