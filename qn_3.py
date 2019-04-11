#Compute the volume of a cylinder
import math as m

def volume():
    rad = eval(input("enter the radius of the cylinder:"))
    height = eval(input("enter the height of the cylinder:"))
    area = m.pi * rad * rad
    print("the area of a cylinder with radius",rad,"is:",area)
    
    volume = area * height
    print("the volume of the rectangle is:",volume)
    
volume()
