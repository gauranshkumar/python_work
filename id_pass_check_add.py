import json
from data_handle import create_member

with open('all_details.json') as f:
    user = json.load(f)

inp = str(input('Enter Username : '))
if inp in user:                                                                
    password_inp = str(input('Enter Password : '))
    if password_inp == user[inp]['pass']:
        print("Your Credentials are : ")
        #for person in data[inp]:
        print('Name : '+inp.capitalize())
        print('Age : '+user[inp]['age'])
        print('Email : '+user[inp]['email'])
        print('Phone Number : '+user[inp]['phone'])
    else:
        print('Password Incorrect')

else:
    print('User does not exist')
    check = input("Do You Want to add ??")
    if check == 'yes' or check == 'y':
        name = input('Enter Name : ')
        email = input('Enter Email : ')
        phone = input('Enter Phone : ')
        age = input('Enter Age : ')
        create_member(name,email,age,phone)

