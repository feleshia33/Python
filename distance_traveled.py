#Exercise #4: Distance Traveled

#speed in MPH
mph = int(input('What is the speed of the vehicle in mph? '))
hours = int(input('How many hours has it traveled? '))

#set distance to zero 
distance = 0

print('Hour\tDistance Traveled')

#print number of hours and distance travled
for num in range(1, hours + 1):
    distance = num * mph
    print(num, '\t', distance)
    
