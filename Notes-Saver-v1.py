'''
📝 Notes Saver v1

Requirements:

Ask the user to enter 5 notes.
Save them in notes.txt.
Read the file.
Print all the notes.
'''
Note1 = input("Enter 1st Note: ")
Note2 = input("Enter 2nd Note: ")
Note3 = input("Enter 3rd Note: ")
Note4 = input("Enter 4th Note: ")
Note5 = input("Enter 5th Note: ")

with open("notes.txt","w") as f:
    f.write(Note1 + "\n")
    f.write(Note2 + "\n")
    f.write(Note3 + "\n")
    f.write(Note4 + "\n")
    f.write(Note5)

with open("notes.txt","r") as f:
    data = f.read()
    print(data)    