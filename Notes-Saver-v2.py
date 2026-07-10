'''
📝 Notes Saver v2
Objective

Instead of saving exactly 5 notes and exiting, the user should be able to choose what they want to do.

Features
========= NOTES SAVER =========

1. Add Note
2. View Notes
3. Exit

Enter your choice:
'''
while True:
    Features = "1. Add Note\n2. View Notes\n3. Exit"
    print(Features)
    choice = int(input("Enter your choice from (1/2/3): "))
    
    if choice == 1:
        with open("notes.txt","a") as f:
            add_note = input("Enter your note: ")
            f.write(add_note + "\n")
            print("Note Saved Successfully")

    elif choice == 2:
        with open("notes.txt","r") as f:
            view_notes = f.read()
            print(view_notes)

    elif choice == 3:
        print("Thank you")
        break
    else:
        print("Invalid Choice")
        break
 
       
