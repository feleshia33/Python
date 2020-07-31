import Baseball

def main():
    #input from user
    name = input("Enter player last name: ")
    atBats = int(input("Enter players number of at bats: "))
    hits = int(input("Enter players number of hits: "))
    average = BA(atBats, hits)
    print(name, 'has a batting average of', format(average, '.3f'))
#func to get average batting average    
def BA(ab,h):
    return ab/h
main()
