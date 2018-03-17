import getpass
import random
import os
import sys


def one():
    passwrd = getpass.getpass("Enter your own password:")
    path = str(web_name)
    os.mkdir(path)
    os.chdir(path)
    file = open('user_' + str(usr_name) + '.txt', 'w')
    file.write('Account for: ' + str(web_name) + '\n' + 'user_name: ' + str(usr_name) + '\n' + 'pass: ' + str(passwrd))
    file.close()
    print("\nYour password has been saved successfully!")
    success()


def two():
    global passwrd_list
    global recomm
    global passwrd
    chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+"
    passwrd_list = []

    recomm = int(input("Enter no. of password recommendations you want:"))
    pass_len = int(input("Enter the desired length of the password:"))
    for p in range(recomm):
        passwrd = ""
        for c in range(pass_len):
            passwrd += random.choice(chars)
        passwrd_list.append(passwrd)
    print("Your %d passwords are:" % recomm)
    print_pass()


def print_pass():
    recomm = 0
    for i in passwrd_list:
        print("%d. %s" % (recomm, i))
        recomm += 1
    print('Choose any one of them:')

    choose = input()

    for h in range(recomm):
        if choose is recomm:
            passwrd_list[recomm] = passwrd
    print("You chose:", passwrd, "password")
    confirm_input()


def confirm_input():
    print("Press Y to confirm your choice or N to retry:")
    retry = input()
    if retry is "Y":
        path = str(web_name)
        os.mkdir(path)
        os.chdir(path)
        file = open('user_' + str(usr_name) + '.txt', 'w')
        file.write(
            'Account for: ' + str(web_name) + '\n' + 'user_name: ' + str(usr_name) + '\n' + 'pass: ' + str(passwrd))
        file.close()
        print("\nYour password has been saved successfully!")
        success()

    if retry is "N":
        print("Choose your password again:")
        print_pass()


def success():
    print("\nDo you want to:\n\n1.View your credentials,\n2.Manage new account, \n3.EXIT")
    success = input()
    if success is "1":
        file = open('user_' + str(usr_name) + '.txt', 'r')
        file_contents = file.read()
        print(file_contents)

        print("What do you want to do now?\n\n1.Manage new account, \n2.EXIT")
        what = input()
        if what is "1":
            main()
        if what is "2":
            sys.exit()


    if success is "2":
        main()
    if success is "3":
        sys.exit()


def main():
    global usr_name
    global web_name
    web_name = input("Enter the website name:")

    usr_name = input("Enter username:")

    main_path = 'C:/Users/Abhishek S Chaudhary/Desktop/Python Projects/'
    os.chdir(main_path)

    select = ("Select an option:")

    print("1: Enter password on your own, \n2: Create a password")

    choice = input()

    if choice.isdigit():

        if choice is "1":
            one()

        if choice is "2":
            two()
    else:
        print("Invalid Option, Kindly try again!")

main()