"""
1404 Practical
get users email and name
store in dictionary
"""

email_name = {}
email = input("Email: ")

while email != " ":
    start = email.split('@')[0]
    parts = start.split('.')
    name = " ".join(parts)
    print(name)
    confirm_name = input(f"Is your name:  {name}, Y/n").upper()

    if confirm_name != "Y" and confirm_name != "":
        name = input("Name: ")
    email_name[email] = name
    email = input("Email: ")

for email, in email_name(email):
    print(name, email)

print(email_name.items())
