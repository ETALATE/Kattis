# Your job is to take a point and determine the quadrant it is in. You can assume that neither of the two coordinates will be 0.
# The first line of input contains the integer x. The second line of input contains the integer y.

x_coordiante = int(input())
y_coordiante = int(input())

if x_coordiante > 0 and y_coordiante > 0:
    print(1)
elif x_coordiante > 0 and y_coordiante < 0:
    print(4)
elif x_coordiante < 0 and y_coordiante < 0:
    print(3)
else: 
    print(2)