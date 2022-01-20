people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby'},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]
for p in people:
    print(p)
    try:
        if p['age'] < 20:
            print("어린이입니다.")
        else:
            print("성인입니다")
    except:
        name = p['name']
        print(f"키 값이 존재하지 않는 변수가 있습니다 = {name}.")