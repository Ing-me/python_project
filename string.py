# This program takes an email address. It cleans the email. And validates the email. 

username = ""
domain = ""

email = input("Enter your email: ")
clean_email = email.strip().lower()
has_at_symbol  =  clean_email.count("@") == 1

if has_at_symbol:
    at_pos = clean_email.index("@")
    username = clean_email[0:at_pos]
    domain = clean_email[at_pos + 1:]
    has_dot = domain.count(".") == 1
    if has_dot:
        print(f"Your email is: {clean_email}")
        print(f"Your username is: {username} and the domain is: {domain}")
    else:
        print("The email is invalid: missing . symbol")
else:
    print("This email is incorrect: missing @ symbol")