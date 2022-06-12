import hashlib


def signup():
    email = input("Enter email address: ")
    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")
    if confirm_password == password:
        # enc = confirm_password.encode()
        # hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.txt", "w") as f:
            f.write(email + "\n")
            f.write(confirm_password)
            # f.write(hash1)
        print("You have registered successfully!")
    else:
        print("Password is not same as above! \n")


def login():
    email = input("Enter email: ")
    password = input("Enter password: ")
    auth = password.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_email, stored_password = f.read().split("\n")

    if email == stored_email and auth_hash == stored_password:
        print("Logged in Successfully!")
    else:
        print("Login failed! \n")


while 1:
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")
