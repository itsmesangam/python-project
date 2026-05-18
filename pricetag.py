#Create one program that display price accourding to the client price
#if amount>+500 print amount is high
#else print amount is low
amount = float(input("enter the total amount:"))
if amount >= 5000:
    return_amount = amount - 5000
    print(f"you have sufficient amount. Retrun money is {return_amount}")

else:
    remaining_amount = amount - 5000
    print(f"you have not sufficient Balance. add blance {remaining_amount} .")
    