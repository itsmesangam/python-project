one_week_expense = [500, 200, 450, 340, 300, 667, 900]
total_number_of_days = len(one_week_expense)
total = sum(one_week_expense)
average = total/total_number_of_days
print(f"total expense is {total}")
print(f"Avg expense is {average: .2f}")
