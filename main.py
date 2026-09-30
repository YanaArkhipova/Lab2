import os

password=input("Enter your password: ")
os.system("cls")
entered_password=input("Password: ")

if entered_password==password:
    print("Password accepted.")
else:
    print("Sorry, that is the wrong password.")
