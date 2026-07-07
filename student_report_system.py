'''
Mini Project 
🟢 Student Management System
Take marks of 5 students.
Store them in a list.
Create separate functions that return:
Highest marks
Lowest marks
Average
Pass count
Fail count
Grade
Grades:
90+  → A
80-89 → B
70-79 → C
60-69 → D
40-59 → E
<40 → Fail
Print all returned values.
Restrictions:
❌ max()
❌ min()
❌ sum()
❌ len()
Use only the concepts you've learned.
'''

marks1 = int(input("Enter 1st Student Marks: "))
marks2 = int(input("Enter 2nd Student Marks: "))
marks3 = int(input("Enter 3rd Student Marks: "))
marks4 = int(input("Enter 4th Student Marks: "))
marks5 = int(input("Enter 5th Student Marks: "))

Total_marks = [marks1,marks2,marks3,marks4,marks5]

def Highest(Total_marks):
    highest = None
    for i in Total_marks:
        if highest is None:
            highest = i
        elif i > highest:
            highest = i
    return highest
print(Highest(Total_marks))        


def Lowest(Total_marks):
    lowest = None
    for i in Total_marks:
        if lowest is None:
            lowest = i
        elif i < lowest:
            lowest = i
    return lowest
print(Lowest(Total_marks))        

def Average(Total_marks):
    Total = 0
    count = 0
    for i in Total_marks:
        Total += i
        count += 1
    return (Total/count)    
print("Average:",Average(Total_marks))


def pass_count(Total_marks):
    count = 0
    for i in Total_marks:
        if i >=40:
            count += 1
    return count
print("Pass Count:",pass_count(Total_marks))        


def fail_count(Total_marks):
    count = 0
    for i in Total_marks:
        if i < 40:
            count += 1
    return count
print("Fail Count:",fail_count(Total_marks))      

def Grades(Total_marks):
    grades = []
    for i in Total_marks:
        if i >= 90:
             grades.append("A")
        elif 80 <= i <= 89:
             grades.append("B")
        elif 70 <= i <= 79:
             grades.append("C")
        elif 60 <= i <= 69:
             grades.append("D")
        elif 40 <= i <= 59:
             grades.append("E")
        else:
             grades.append("Fail")
    return grades
print(Grades(Total_marks))        
            