class Rectangle():
	def __init__(self,length,width):
		self.length = length
		self.width = width
		self.area = length * width

class Circle():
	def __init__(self,radius):
		self.pi = 3.14159265359
		self.radius = radius
		self.area = self.pi * (radius * radius)

User_input = input(':')

if User_input == 'Rectangle':
	R1 = Rectangle(input("length:"),input("width:"))
	print R1.area
if User_input == 'Circle':
	C1 = Circle(input('Radius:'))
	print C1.area