x1=int(input("Upper left point x: "))
y1=int(input("Upper left point y: "))

x2=int(input("Right lower point x: "))
y2=int(input("Right lower point y: "))

x=int(input("Coordinates of the point (x): "))
y=int(input("Coordinates of the point (y): "))

if x >= x1 and x <=x2:
    print("Yes")
elif y >= y1 and y <=y2:
    print("Yes")
else:
    print("No")
