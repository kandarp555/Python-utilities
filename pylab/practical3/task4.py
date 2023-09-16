#Circle Area and Perimeter
class Circle:
    def __init__(self,radius):
        self.radius = float(radius);
    def area(self):
        area = float(self.radius*self.radius*3.14)
        print("Area of the circle is: %d"%area)
    def perimeter(self):
        perimeter = float(2*3.14*self.radius)
        print("Perimeter of the circle is: %d\n"%perimeter)
r = input("Enter the radius of c1 instance:\n")
c1 = Circle(r)
c2 = Circle(r)
c1.area()
c1.perimeter()
print("Calling with c2 instance with same radius:\n")
c2.area()
c2.perimeter()
r1 = input("Modify the radius of c2 instance:\n")
c2 = Circle(r1)
c2.area()
c2.perimeter()