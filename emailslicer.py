# Email Slicer Using Python

print("Enter your email Id: ")
email = input().strip()

if email.find("@") != -1:
    username = email[:email.index("@")]
    domain = email[email.index("@")+1:]
    print("Your Username is: ",username)
    print("Domain is: ",domain)
else:
    print("Please Enter a valid Email Id.")
