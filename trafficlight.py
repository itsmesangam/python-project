#use multiple condition using elif loop
#Traffic light concept
light = input("enter traffic light colour. [Red, Yellow, Green]: ").lower()

if light == "red":
    print("stop!")
elif light == "Yellow":
    print("ready to move")
elif light == "green":
    print("You can go")
else:                               #use  else at last if necessary.
    print("invalid colour")


    