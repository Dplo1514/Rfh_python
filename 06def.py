def check_gender(pin):
    num = pin.split("-")[1][:1]
    if int(num) % 2 == 0:
        print("your girl")
    else:
        print("your boy")

check_gender("980304-2852220")