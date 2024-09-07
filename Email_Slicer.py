email = input("Please  Enter Your Email Address : ")

index = email.index("@")

username = email[:index]
domain = email[index+1:]


print(f"Your Username is{username} and domain is {domain}")
