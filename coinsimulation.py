import random
from PIL import Image
head = Image.open("/home/gagan/Desktop/head.jpeg")
tail = Image.open("/home/gagan/Desktop/tail.jpeg")
list = [head, tail]
def simulation(n):
    head1 = 0
    tail1 = 0
    for i in range(n):
        rand = random.choice(list)  
        if rand == head:
            head1 += 1
            head.show()     
        else:
            tail1 +=1
            tail.show()
    print("the number of head is:",head1)
    print("the number of tail is:",tail1)
simulation(5)
