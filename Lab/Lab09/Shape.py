class Rectangle:
	def __init__(self,width,length) :
		self.width =  width 
		self.length = length
	def area(self) :
		return self.width * self.length
	def perimeter(self) :
		return 2*(self.length + self.width)
	def is_square(self) :
		if self.length == self.width :
			return 'This rectangle is square too.'
		return 'This rectangle is not square.'

def test_rectangle():
	length = int(input("Enter rectangle length : "))
	width = int(input("Enter rectangle width : "))
	#width,length = 5,5
	p1 = Rectangle(length,width)
	print(f"Area is {p1.area()}.")
	print(f"Perimeter is {p1.perimeter()}.")
	print(p1.is_square())

test_rectangle()

class Triangle:
	def __init__(self,l1,l2,l3) :
		self.l1 = l1
		self.l2 = l2
		self.l3 = l3
	def area(self) :
		s = (self.l1 + self.l2 + self.l3)/2
		return ( s* (s-self.l1)* (s-self.l2) *(s-self.l3) )**0.5
	def perimeter(self) :
		return self.l1 + self.l2 + self.l3
	def is_right_triangle(self) :
		if self.l1**2 + self.l2**2 == self.l3**2 or self.l3**2 + self.l2**2 == self.l1**2 or self.l1**2 + self.l3**2 == self.l2**2 :
			return 'This triangle is right triangle too.'
		return 'This triangle is not right triangle.'

def test_triangle():
	l1 = int(input('Enter triangle first side length : '))
	l2 = int(input('Enter triangle second side length : '))
	l3 = int(input('Enter triangle third side length : '))
	#l1,l2,l3 = 3,4,3
	p2 = Triangle(l1,l2,l3)
	print(f"Area is {p2.area()}.")
	print(f"Perimeter is {p2.perimeter()}.")
	print(p2.is_right_triangle())

test_triangle()

pi = 3.14
class Circle() :
	def __init__(self,r) :
		self.r = r 
	def area(self) :
		return pi*(self.r**2)
	def perimeter(self) :
		return 2*pi*self.r

def test_circle() :
	r = int(input("Enter circle radius : ")) 
	#r = 7 
	p3 = Circle(r)  
	print(f'Area is {p3.area():.2f}.')  
	print(f'Perimeter is {p3.perimeter():.2f}.')

test_circle()



