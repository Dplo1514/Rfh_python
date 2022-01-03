li = [1,2,3,4,5]
dic = {"num1" : 1 , "num2" : 2 , "num3" : 3}
result = 5 in li
print(li , dic["num1"] , result)

# smith 의 sience점수 출력
people = [
    {'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
    {'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
    {'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
    {'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
]

print(people[2]["score"]["science"])