weight = float(input("Enter Your Weight : "))
unit = input("Enter the Unit  (K or L) :")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs"
    print(f" your Weight is: {round(weight,1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs"
    print(f" your Weight is: {round(weight,1)} {unit}")

else:
    print("{unit} is invalid")


 
    