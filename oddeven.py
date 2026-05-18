#this is the program to check odd and even number 
#if the number is devisible by 2 is even and not divisible by 2 is odd.
number = int(input("Enter the number: "))
#user input the int number in variable
if number % 2 == 0:     #loop start here and codition appply
    print("This is Even Number")
else:
    print("This is Odd Number")
