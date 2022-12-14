import string
ad_usrs = {'admin':'Sous-Do'}
users = {'admin':'Sous-Do'}
caps = string.ascii_uppercase
numbers = []
for i in range(10):
    numbers.append(str(i))
special_char = ['!', '?', '@', '#', '$']
name_check = False

def name_availible(name):
    if name.title() in users:
        return False
    else:
        return True

def number_found(name):
    found = False
    for number in numbers:
        if name.find(number) > -1:
            found = True
    return found

def caps_found(pw):
    found = False 
    for letter in caps:
        if pw.find(letter) > -1:
           found = True
    return found 

def specialchar_found(pw):
    found = False 
    for char in special_char:
        if pw.find(char) > -1:
           found = True
    return found 

def ad_login(name):
    found = False
    if name in ad_usrs:
        found = True
    return found

def usr_login(name):
    found = False
    if name in users:
        found = True
    return found
def log_in_check(user):
    found = False
    if user in users:
        found = True
    return found 
     
def passwd_check(found):
    found = False 
    if users.get(log_in):
        found = True
        return found

def create_usr():
    new_usr = dict()
    name_check = False
    while True:
        if not name_check:
            username = input('Create a username: ').lower()
            if name_availible(username):
                if not number_found(username):
                    if 2 < len(username) < 15:
                        name_check = True
                        print('Username created')
                    else:
                        print('name must contain between 2 and 15 characters')
                else:
                    print('username cannot contain numbers')
            else:
                print('Please choose another username')
            password = input('Create a password: ')
            if caps_found(password):
                    if specialchar_found(password):
                        if number_found(password):
                            if len(password) > 7:
                                print(f'your username is {username} and your password is {password}')
                                new_usr[username] = password
                                users.update(new_usr)
                                with open('users.json', 'w') as outfile:
                                    json.dump(new_usr, outfile)
                                return print(users)
                                
                            else:
                                print('Password must contain 8 characters or more')
                        else:
                            print('Password must contain a number')
                    else:
                        print('Password must contain a special character(!, ?, @, #, $)')
                        continue
            else:
                print('Password must contain a capital letter')
                continue
