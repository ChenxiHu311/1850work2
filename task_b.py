grade = input("Please enter a numerical grade:")
if grade.isdigit():
   grade = int(grade)
   if grade < 0 or grade > 100:
    print("Error: Grades must be between 0 and 100")
   else:
    if grade <=100 and grade >= 80:
        print("Your grade is: A")
    elif grade <= 79 and grade >= 60:
        print("Your grade is: B.")
    elif grade <= 59 and grade >= 40:
        print("Your grade is: C.")
    elif grade <= 49 and grade >= 40:
        print("Your grade is: D")
    else:
        print("Your grade is: F")
else:
   print("Error: Please enter a number")