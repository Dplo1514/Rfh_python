# def cal(*args): #함수의 인자를 무제한으로 받음
#     for name in args:
#         print(f"{name}아 밥먹어라")
# cal("임인혁" , "양서연")

def cal(**kwargs):
    print(kwargs)

cal(name = "bob" , age =30 , height = 160)