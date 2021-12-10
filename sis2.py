#Toya West
#Program Status:


 
def main():
    courseDic = {}
    roomsDic = {}
    instructorsDic = {}
    timesDic = {}
 
    while True:
        #get course info
        course = input('Enter a new course number of interest or press enter zero to stop: ')
        if course =="0":
            break
        rooms = input('Enter the course meeting room: ')
        instructors = input('Enter course Instructor''s name: ' )
        times = input('Enter course meeting time: ')
        print("")

    #add course info to dictionaries
        roomsDic[course] = [rooms]
        instructorsDic[course] = [instructors]
        timesDic[course] = [times]

    #used print to test the dictionaries
        print(roomsDic)
        print(instructorsDic)
        print(timesDic)

    
    for course in rooms:
        print('For Course', course, ':')
        print('The Meeting Room is:', roomsDic[course])
        print('The Instructor is:', instructorsDic[course])
        print('The Meeting Time is:', timesDic[course])
    else:
        print(course, 'is an invalid course number.')

    




main()


