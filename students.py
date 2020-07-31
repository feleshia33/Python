#open file for reading
infile = open("students.txt", "r")

#create an empty list
student_data = []
avg_hours = []
total = 0

#reads first line
temp = infile.readline()

#loop thru file
while temp !="":
    #split and append to empty list
    student_data.append(temp.split())
    total +=1
    
    #update with next line
    temp = infile.readline()
    
   
print("Major of last record:", student_data[4][3])
print("Last name of first record:", student_data[0][1])


    
