def check(pin):
    num = pin.split("-")[1][0]
    if num == "1" :
        print("남성입니다.")
    else:
        print("여성입니다")

boy = "102390-1231234"
girl = "161616-2638"

check(boy)
