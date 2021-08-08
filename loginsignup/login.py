print("****wel come to login or sign****")
user=input("do you want to sign up and login:- ")
if user=="login":
    name=input("enter your name")
    last_name=input("enter your last name")
    password=input("enter the password")
    conform_password=input("enter the conform password")
    if "@" in password or "#" in password:
        if password==conform_password:
            print("your accout has create succsecfull! *hureeeeee*")
            a=open("login.txt","w")
            new_file=a.write(name)
            new_file=a.write("\n")
            new_file=a.write(last_name)
            new_file=a.write("\n")
            new_file=a.write(password)
            new_file=a.write("\n")
            a.close()
        else:
            print("your password is wrong")
    else:
        print("special caracter not in a password")        
elif user=="sign":
    name1=input("enter your name")
    file=open("login.txt","r")

    new_file1=file.read()
    if name1 in new_file1:
        password1=input("enter your password")
        if password1 in new_file1:
            print("**login Sucussesfull**")
        else:
            print("your password is wrong!")
    else:
        print("username is wrong!")