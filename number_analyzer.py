'''
🔴 E. Mini Project 3 — Number Analyzer

Create functions to:

Print the square
Print the cube
Check even/odd
Print multiplication table
Print factors (if you know them)

Call all these functions for one user-entered number.
'''
n = int(input("Enter a Number: "))

def sq():
    square = n*n
    print(square)

sq()    

def cu():
    cube = n*n*n
    print(cube)
cu()    

def Check():
    if n%2 == 0:
            print("EVEN")
    else:
            print("ODD")

Check()

def Multiplication_table():
    for i in range(1,11):
        table = n*i
        print(table)  
Multiplication_table()

def factor():
     i = 1
     while i < (n + 1):
          if n%i == 0:
               factor = i
               print(factor)   
          i += 1
                      
factor()
     
      
                 