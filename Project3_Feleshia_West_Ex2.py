#Exercise 2: Areas of Rectangles

area1 = float(input('What is the area of rectangle 1? '))
length1 = float(input('What is the length of rectangle 1? '))
area2 = float(input('What is the area of rectangle 2? '))
length2 = float(input('What is the length of rectangle 2? '))

rec1 = area1 * area1 * length1 * length1
rec2 = area2 * area2 * length2 * length2

if rec1 > rec2:
    print("Rectangle1 has a greater area than rectangle2.")
elif  rec1 < rec2:
    print("Rectangle2 has a greater area than rectangle1.")
else:
    print("The both rectangles area are the same.")
    
