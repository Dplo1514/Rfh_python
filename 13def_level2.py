def cal(*args): #*args 매개변수를 무제한으로 받을 수 있다.
    for li in args:
        print(f'{li} args사용!!')

def cal_1(**kwargs): #**kwargs 매개변수를 받아 딕셔너리로 만들어준다.
    print(kwargs)

result = cal(1,2,3,4,5,6,7,7,8,8,8,8,9,9)
cal_1(name = 'bob' ,age = 24 , height = 160)