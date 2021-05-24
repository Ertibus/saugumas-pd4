import os

from program.crypto.pbkdf2 import PBKDF2Hasher as Hasher
from program.crypto.aes import AESCipher as AES

class FileMG:
    DIR  = "data/"
    FILE = "_data.csv"

    key = ""
    user = ""
    salt_ud = ""

    @classmethod
    def any_user(cls):
        return len(os.listdir(cls.DIR)) == 0

    @classmethod
    def new_file(cls, username:str):
        if os.path.isfile(cls.DIR + username + cls.FILE) and os.stat(cls.DIR + username + cls.FILE).st_size != 0:
            raise ValueError("User already has a file!") 
        else:
            if not os.path.isdir(cls.DIR):
                os.mkdir(cls.DIR)

    @classmethod
    def register_user(cls, login:str, password:str):
        cls.new_file(login)
        cls.user = login
        cls.key = login+password
        hash_salt, hash_pwd = Hasher.encrypt(password)
        with open(cls.DIR + login + cls.FILE, "w") as file:
            file.write(login + ', ' + str(hash_salt) + ', ' + str(hash_pwd) + '\n')
        try:
            cls.encrypt_file()
        except Exception as err:
            raise Exception(err)
        finally:
            cls.user=" "
            cls.key=" "
    
    @classmethod
    def logout(cls ):
        try:
            cls.encrypt_file()
        except Exception as err:
            raise Exception(err)
        finally:
            cls.user=" "
            cls.key=" "

    @classmethod
    def new_password(cls, login:str, password:str, appurl:str, desc:str):
        cryptor = AES(cls.key)
        enc_pwd = cryptor.encrypt(password).hex()

        with open(cls.DIR + cls.user + cls.FILE, "a") as file:
            file.write(login + ', ' + enc_pwd + ', ' + appurl + ', ' + desc + '\n')

    @classmethod
    def update_password(cls, login:str, password:str, appurl:str, desc:str):
        if not os.path.isfile(cls.DIR + cls.user + cls.FILE) or os.stat(cls.DIR + cls.user + cls.FILE).st_size == 0:
            raise Exception("Users file not found")

        cryptor = AES(cls.key)
        enc_pwd = cryptor.encrypt(password).hex()

        out_string = ""
        with open(cls.DIR + cls.user + cls.FILE, "r") as file:
            f_data = file.read()
            userdata = f_data.split('\n')
            out_string += userdata[0] + '\n'
            for entry in userdata[1:]:
                if entry.split(', ')[0] == login:
                    out_string += login + ', ' + enc_pwd + ', ' + appurl + ', ' + desc + '\n'
                else:
                    out_string += entry + '\n'
        print(out_string) 
        with open(cls.DIR + cls.user + cls.FILE, "w") as file:
            file.write(out_string)

    @classmethod
    def delete_password(cls, login:str):
        if not os.path.isfile(cls.DIR + cls.user + cls.FILE) or os.stat(cls.DIR + cls.user + cls.FILE).st_size == 0:
            raise Exception("Users file not found")

        out_string = ""
        with open(cls.DIR + cls.user + cls.FILE, "r") as file:
            f_data = file.read()
            userdata = f_data.split('\n')
            out_string += userdata[0] + '\n'
            for entry in userdata[1:]:
                if entry.split(', ')[0] == login:
                    continue
                else:
                    out_string += entry + '\n'
        print(out_string) 
        with open(cls.DIR + cls.user + cls.FILE, "w") as file:
            file.write(out_string)


    @classmethod
    def login_user(cls, login:str, password:str):
        cls.user = login
        cls.key = login+password
        cryptor = AES(cls.key)
        if not os.path.isfile(cls.DIR + login + cls.FILE) or os.stat(cls.DIR + login + cls.FILE).st_size == 0:
            raise Exception("Users file not found")
        with open(cls.DIR + login + cls.FILE, "rb") as file:
            f_data = file.read()
            dec_data = ""
            try:
                dec_data = cryptor.decrypt(f_data).decode("utf-8")
            except Exception as err:
                cls.user=" "
                cls.key=" "
                raise ValueError("Failed to decrypt file, Bad password or username")
            userdata = (dec_data.split('\n', 1)[0]).split(', ')
            cls.salt_ud = userdata[1]
            pass_ud = userdata[2]
            _, pass_ex = Hasher.encrypt(password, cls.salt_ud) 
            if login != userdata[0] or pass_ex != pass_ud:
                raise ValueError("Bad password or username")
        with open(cls.DIR + login + cls.FILE, "w") as file:
            file.write(dec_data)

    @classmethod
    def encrypt_file(cls):
        if cls.user.isspace() or cls.key.isspace():
            return
        cryptor = AES(cls.key)
        f_data = ""
        with open(cls.DIR + cls.user + cls.FILE, 'r') as file:
            f_data = file.read()
        with open(cls.DIR + cls.user + cls.FILE, 'wb') as file:
            cls.en_data = cryptor.encrypt(f_data)
            file.write(cls.en_data)

    @classmethod
    def get_all_passwords(cls):
        if not os.path.isfile(cls.DIR + cls.user + cls.FILE) or os.stat(cls.DIR + cls.user + cls.FILE).st_size == 0:
            raise Exception("Users file not found")

        with open(cls.DIR + cls.user + cls.FILE, "r") as file:
            f_data = file.read()
            userdata = f_data.split('\n')[1:]
            entry_list = []
            for entry in userdata:
                entry_list.append(entry.split(', '))
            return entry_list

    @classmethod
    def get_search_results(cls, login_target):
        if not os.path.isfile(cls.DIR + cls.user + cls.FILE) or os.stat(cls.DIR + cls.user + cls.FILE).st_size == 0:
            raise Exception("Users file not found")

        with open(cls.DIR + cls.user + cls.FILE, "r") as file:
            f_data = file.read()
            userdata = f_data.split('\n')[1:]
            entry_list = []
            for entry in userdata:
                esplit = entry.split(', ') 
                if login_target in esplit[0]:
                    entry_list.append(esplit)
            return entry_list

    @classmethod
    def show_password(cls, password):
        cryptor = AES(cls.key)
        return cryptor.decrypt(bytes.fromhex(password)).decode('utf-8')
