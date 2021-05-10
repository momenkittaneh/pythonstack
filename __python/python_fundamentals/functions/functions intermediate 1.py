import random
def randInt(min=0, max=100):
    if min>max:
        print(f"please provide number larger than= {min}")
        return
    elif: max<0:
        print(f"please provide number larger than zero,your number is {max}")
    num=random.random() * (max-min) + min
    return num

