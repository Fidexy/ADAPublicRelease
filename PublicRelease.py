from FixNum import FixNum

%load_ext autoreload
%autoreload 2

userinput = input("Number of decimal places (default 2): ")    
prec = int(userinput) if userinput else 2
def Menu():
    while True:
        print("Menu:\n [a] Fixed-point [operation] \n [b] Fixed-point power operation \n [x] Exit")
        choice = input("Enter your choice: ")
        if choice == 'a':
            print("Fixed-point [operation] selected (x+y).")
            # Task code goes here
        elif choice == 'b':
            print("Fixed-point power operation selected (x^y).")
            # Distinction code goes here
        elif choice == 'x':
            print("Exiting the menu.")
            break
        else:
            print("Invalid choice. Please try again.")
Menu()