import json
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggenIn = False
        self.currentUser = {}

        # load users from .json file
        self.loadUser()

    def loadUser(self):
        pass
    def register(self, user: User):
        self.users.append(user)
        #self.savetoFile()
        print("Kullanıcı Oluşturuldu!")
    def login(self):
        pass
    def savetoFile(self):
        list =[]
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        
        with open("C:\\users.json",'w') as file:
            json.dump(list,file)

repository = UserRepository()

while True:
    print('Menü'.center(50,"*"))
    secim = input("1- Register\n2- Login\n3- Logout\n4- identity\n5- Exit\nSeçiminiz: ")
    if secim =='5':
        break
    else:
        if secim == '1':
            #register
            username = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")
            user = User(username=username, password=password, email=email)
            repository.register(user)

        elif secim == '2':
            #Login
            pass
        elif secim == '3':
            #Logout
            pass
        elif secim == '4':
            #identity (display username)
            pass
        else:
            print("Yanlış seçim!")

































