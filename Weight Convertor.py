weight = float(input("Enter Your Weight : "))
unit = input("Enter the Unit  (K or L) :")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs"
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs"

else:
    print("{unit} is invalid")


print(f" your Weight is: {weight} {unit}")
    