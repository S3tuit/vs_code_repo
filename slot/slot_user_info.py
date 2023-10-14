import pickle

def update_data():
    global users_data
    with open("C:\\Users\\matte\\OneDrive\\Desktop\\GitHub\\vs_code_repo\\slot\\user_data.pkl", "wb") as file:
        pickle.dump(users_data, file)

def delete_user(key):
    global users_data

    with open("C:\\Users\\matte\\OneDrive\\Desktop\\GitHub\\vs_code_repo\\slot\\user_data.pkl", "rb") as file:
        users_data = pickle.load(file)
    del users_data[key]
    update_data()

def update_users(key, values):
    global users_data

    with open("C:\\Users\\matte\\OneDrive\\Desktop\\GitHub\\vs_code_repo\\slot\\user_data.pkl", "rb") as file:
        users_data = pickle.load(file)

    users_data[key]= values
    update_data()

users_data = {}