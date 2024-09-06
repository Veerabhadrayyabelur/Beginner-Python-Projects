unit = input("May i know temperature Conversion unt (C or F) : ")
temp = float(input("enter the temperature : "))

if unit == "C" or unit =="c":
    temp  = round((9 * temp)/ 5 +32.5 , 1)
    print(f" the temperature in fahrenheit is  :{temp} °F ")
  
elif unit == "F" or unit == "f":
     temp  = round((temp - 32 )*5 /9 , 1)
     print(f" the temperature in Celsius is :{temp} °C ")


else:
    print("{unit} is invalid")