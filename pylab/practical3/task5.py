# Complex Number Operations
import cmath


class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        print(f"Complex number: {self.real} + {self.img}j")

    def add(self, other):
        result_real = self.real + other.real
        result_img = self.img + other.img
        print(f"Addition result: {result_real} + {result_img}j")

    def modulus(self):
        mod = cmath.sqrt(self.real**2 + self.img**2)
        print(f"Modulus: {mod}")


# Taking user input for the first complex number
real = float(input("Enter the real number for n1: "))
img = float(input("Enter the imaginary number for n1: "))
n1 = ComplexNumber(real, img)

# Taking user input for the second complex number
real1 = float(input("Enter the real number for n2: "))
img1 = float(input("Enter the imaginary number for n2: "))
n2 = ComplexNumber(real1, img1)

# Performing addition of the two complex numbers
print("\nAddition of two instances:")
n1.add(n2)

# Calculating modulus of n1 and n2
print("\nModulus of n1:")
n1.modulus()
print("Modulus of n2:")
n2.modulus()

# Deleting the imaginary part of n2 instance
del n2.img

# Checking imaginary parts
print("\nChecking for the imaginary parts:")
print("For n1 instance:")
if hasattr(n1, "img"):
    print("Imaginary part is present")
else:
    print("Imaginary part is not present")

print("For n2 instance:")
if hasattr(n2, "img"):
    print("Imaginary part is present")
else:
    print("Imaginary part is not present")
