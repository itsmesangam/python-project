#login username and password using if loop in python
username = "admin"
userpassword = "admin123"

input_user = str(input("enter username:"))
input_password = input("enter password:")

if input_user == username and input_password == userpassword:
    print("Login Successful")
else:
    print("unable to login.")

