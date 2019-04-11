import random

def diceroll(n):
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    for i in range(n):
        rand = random.randint(1,6)
        if rand == 1:
            one += 1
        elif rand == 2:
            two +=1
        elif rand == 3:
            three +=1
        elif rand == 4:
            four +=1
        elif rand ==5:
            five +=1
        else:
            six += 1
    print("the number of ones", one)
    print("the number of twos", two)
    print("the number of threes", three)
    print("the number of fours", four)
    print("the number of fives", five)
    print("the number of sixes", six)

diceroll(40)
