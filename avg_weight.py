# This program averages weekly weight. It ask the user for the
# their weight each Saturday of the month for an average monthly weight.

# Get the number of weeks
week = int(input("Enter the number of weeks: "))

# Get the number of weigh-ins
weigh_ins = int(input("Enter the number of weigh ins: "))

# Determine average from weigh-ins

for weigh in range(week):
    # Initialize an accumulator
    total = 0.0
    # Get weekly weigh-ins
    print("Client", weigh + 1)
    print("---------------")
    for weigh_num in range(weigh_ins):
        print("Weigh in #", weigh_num +1, end="")
        count = float(input(": "))
        total += count

    # Calculate average
    average = total / weigh_ins
    print()

    # Display average
    print("The average for client number", weigh + 1,
          "is: ", average)

    print()
    
