username = input("Enter username")
password = input("Enter password")
if username == "admin" and password == "1234":
    print("login success")
else:
    if username != "admin":
        print("username is wrong")
    else:
        print("wrong password")
