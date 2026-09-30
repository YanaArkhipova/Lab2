x1=int(input('Coordinates of the 1 point (x): '))
y1=int(input('Coordinates of the 1 point (y): '))

x2=int(input('Coordinates of the 2 point (x): '))
y2=int(input('Coordinates of the 2 point (y): '))

x3=int(input('Coordinates of the 3 point (x): '))
y3=int(input('Coordinates of the 3 point (y): '))

a=(x1-x2)**2 + (y1-y2)**2
b=(x1-x3)**2 + (y1-y3)**2
c=(x2-x3)**2 + (y2-y3)**2

if a+b==c or a+c==b or b+c==a:
    print("Yes")
else:
    print("No")
