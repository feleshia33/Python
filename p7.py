#opens file
infile = open("students.txt", "r")
#create an empty list
student_list = []
#accululator for total
total = 0
#read first line 
temp = infile.readline()
#read lines until empty and splits list
#and append to student list
while temp !="":
    #split elements and appends to student list 
    student_list.append(temp.split())
    temp = infile.readline()
    #length of student list
    num = len(student_list)
print("Major for the last record:", student_list[4][3])
print("Last name of the first record:", student_list[0][1])
#loops thru student list indexing hours  
for row in student_list:
    for hours in row[-1:]:
        list = hours
        list = [hours]
        #converts str to int
        for i in list:
            total += int(i)
print("Average number of hours:", total/num)

    


    
    

    




