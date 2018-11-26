#GRADE CALCULATOR
x=eval(input('Enter score in the Course:'))

if x==70 or x>70:
    print('your Grade is A')
if x<70 and x>60:
    print('your Grade is B')
if x<60 and x>50:
    print('your Grade is C')
if x<50 and x>40:
    print('your Grade is D')
if x<40:
    print('your Grade is F')
