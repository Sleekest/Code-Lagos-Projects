print('Hello Instructor')

#import complex math module
import cmath
a=float(input('Enter your a:'))
b=float(input('Enter your b:'))
c=float(input('Enter your c:'))
z=(b**2)-(4*a*c)
x=(-b-cmath.sqrt(z))/(2*a)
y=(-b+cmath.sqrt(z))/(2*a)
print('The answer is as follows:',x,y)

