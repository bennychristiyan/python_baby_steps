#slicing an email address into username and domain name
email = input("Enter your email address: ").strip()
user = email[:email.index("@")]
domain = email[email.index("@") + 1:]
output = "Your username is {} and your domain name is {}".format(user, domain)
print(output)

"""

Enter your email address: bennychristiyan89@gmail.com
Your username is bennychristiyan89 and your domain name is gmail.com

"""