# things needed
# store user info (using a text document)
# make random combinations pop up
# calculate the win 
# add the win to user info

# id — username — password — balance

import pickle
import random as rm
import slot_user_info as sui

class User:
    
    def __init__(self, id, user_name, password, balance) -> None:
        self.id = id
        self.user_name = user_name
        self.password = password
        self.balance = balance

class Casino:
    def __init__(self, users_list=[], users_name_list=[], users_info={}) -> None:

#load the data of the users
        try:
            with open("C:\\Users\\matte\\OneDrive\\Desktop\\GitHub\\vs_code_repo\\slot\\user_data.pkl", "rb") as file:
                self.users_info = pickle.load(file)
                self.users_list = list(self.users_info.keys())
                self.users_name_list = list(users_name_list)
                for i in self.users_info.keys():
                    self.users_name_list.append(self.users_info[i]["user_name"])
        except (FileNotFoundError, EOFError) as e:
            print(f"Error loading user data: {e}")

    def user_registration(self):
        user_name = input("Insert an username: ")

#make sure that there are no equal user names
        if user_name in self.users_name_list:
            print("Username already exists! Retry...")
            self.user_registration()
        elif user_name == "cancel":
            pass
        else:
            while True:
                password_try = input("Insert a password: ")
                password_try_2 = input("Confirm password: ")
                if password_try_2 == password_try:
                    password = password_try_2
                    break
                else:
                    print("Passwords do not match! Retry...")
        
#make sure there are no equal users ids
            while True:
                random_number = rm.randint(0, 999)
                user_id = f"User{random_number:03d}"
                if user_id in self.users_list:
                    pass
                else:
                    break

#register a user in the class User and update
#all the Casino lists and dicts
            new_user = User(user_id, user_name, password, balance=0)
            self.users_list.append(user_id)
            self.users_name_list.append(user_name)
            new_user_info = {"user_name": user_name, "password": password, "balance": 0}
            self.users_info[user_id] = new_user_info
            print("User registered successfully!")
            sui.update_users(user_id, new_user_info)

    def delete_profile(self):
        user_name_del = input("Username of the account you wish to delete: ")
        count = 0

#check if there's an account with that username
        for i in self.users_info.keys():
            if user_name_del in self.users_info[i]["user_name"]:
                count += 1
                password_del = input("Insert the password: ")
#check if password correspond
                if password_del == self.users_info[i]["password"]:
                    sui.delete_user(i)
                    print("User deleted!")
                else:
                    print("Password does not correspond!!")
            else:
                pass
        if count == 0:
            print("This username doesn't have an account :()")

    def play_slot():
        pass

    def withdraw():
        pass

    def deposit():
        pass



casino = Casino()

casino.delete_profile()