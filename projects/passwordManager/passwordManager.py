from cryptography.fernet import Fernet
import sys

# generate key, run only once for generating key
def write_key():
    key= Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)        
write_key()

def load_key():
    file = open("key.key",'rb')
    key = file.read()
    file.close()
    return key

key = load_key() 
fer = Fernet(key)

def view():
    acName = input('Enter your account name: ')
    with open('password.txt','r') as pfile:
        for line in pfile.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            user = user.strip()
            if user == acName: 
                print(f"User : {user} | Password: {fer.decrypt(passw.encode()).decode()}")
                sys.exit(1)
        print(f"User with the account name {acName} doesn't exist.")


def add():
    name = input("Account name: ")
    pwd = input("Account Password: ")
    with open ('password.txt','a') as pfile:
        pfile.write(f"{name} | {(fer.encrypt(pwd.encode())).decode()}\n")

while True:
    mode = input("Wanna add a new or view the password? (add , view). Press q to quit : ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode! Select a valid one.")
        continue

