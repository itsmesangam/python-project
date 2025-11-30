"""write a program to calculate what you spend each month  from 
   Jan to Dec using a list and add them up to find the total expense of the year
   and figure out the average expense per month"""
   #expense calculate 
expenses = [2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500]
total_expense = sum(expenses)
average_expense = total_expense / 12
print(f"Total expense of the year is {total_expense}")
print(f"Average expense per month is {average_expense}")
