#suppose you often go to the resturant with friends and you have to splite amount of bill.
#write a program to calculate the splite amount of bill.
#formula total_boll_amount/number_of_friend
#use user input 

total_expense = float(input("total expense amount: "))
number_of_friends = int(input("total friends: "))
splite_amount = total_expense/number_of_friends
print(f"per person expense amount is {splite_amount: .2f}")



