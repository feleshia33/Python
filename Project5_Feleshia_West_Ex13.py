#Exercise #13: Falling Distance

def falling_distance():
    g = 9.8
    print("Seconds\tDistance(m)")
    for distance in range(1,10 +1):
        dist = ((1/2 * g) * distance**2)
        print(distance, "\t",format(dist, '.2f'))

falling_distance()    
    
