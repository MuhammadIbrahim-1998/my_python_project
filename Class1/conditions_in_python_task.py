marks_input = input("Enter student's marks (or type 'A' if absent): ")

passing_marks = 50

if marks_input.upper() == "A":
    print("Student is Absent.")
else:
    try:
        marks = float(marks_input)

        if marks > passing_marks:
            print("Student has Passed.")
        elif marks < passing_marks:
            print("Student has Failed.")
        elif marks == passing_marks:
            print("Student has Barely Passed.")
    except ValueError:
        print("Invalid input. Please enter a number or 'A' for absent.")
