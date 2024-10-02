import sys


def main():
    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        user_choice = input("Type the number of the desired choice: ")
        if user_choice == "1":
            encrypted_file = input("Please input the name of the text file that you would like to encrypt (include the file extension): ")
            if encrypted_file != "password.key" and encrypted_file != "encrypted.txt":
                fileEncrypt(encrypted_file)
                print("")
            else:
                sys.exit("Restricted file name.\n")
        elif user_choice == "2":
            decrypted_file = input("Please input the name of the text file that you would like to decrypt to (include the file extension): ")
            if verification_pin():
                if decrypted_file != "password.key" and decrypted_file != "encrypted.txt":
                    fileDecrypt(decrypted_file)
                    print("")
                else:
                    sys.exit("Restricted file name\n")
            else:
                print("Password does not match\n")
        elif user_choice == "3":
                sys.exit()
        else:
                print(f"{user_choice} is not a valid option.\n")


def generate_pin():
    password = input("Please create your 6-Digit pin: ")
    if password.isnumeric() and len(password) == 6:
        try:
            with open("password.key", "w") as file:
                file.write(password)
                return True
        except Exception as error:
            print(f"Unexpected error has occured while reading or writing: {error}\n")
    else:
        print("Password does not meet qualifications\n")
    
    return False


def verification_pin():
    password = input("Please enter your 6-digit pin: ")
    if password.isnumeric() and len(password) == 6:
        try:
            with open("password.key", "r") as check:
                if check.readline().strip() == password:
                    return True
        except Exception as error:
            print(f"Unexpected error has occured while reading or writing: {error}\n")
    
    return False


def encrypt(lines):
    encrypted_text = ""
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    special_char = "\"!@#$%^&*()-_=+[{]}\\|;:,<.>/?`'~"
    reversed_alphabet= alphabet[::-1]
    reversed_special = special_char[::-1]

    for line in lines:
        for char in line:
            if char.isalpha():
                index = alphabet.index(char.lower())
                if char.islower():
                    encrypted_text += reversed_alphabet[index]
                else:
                    encrypted_text += reversed_alphabet[index].upper()
            elif char in special_char:
                index = special_char.index(char)
                encrypted_text += reversed_special[index]
            else:
                encrypted_text += char
        
    return encrypted_text


def decrypt(lines): 
    decrypted_text = ""
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    special_char = "\"!@#$%^&*()-_=+[{]}\\|;:,<.>/?`'~"
    reversed_alphabet= alphabet[::-1]
    reversed_special = special_char[::-1]

    for line in lines:
        for char in line:
            if char.isalpha():
                index = reversed_alphabet.index(char.lower())
                if char.islower():
                    decrypted_text += alphabet[index]
                else:
                    decrypted_text += alphabet[index].upper()
            elif char in special_char:
                index = reversed_special.index(char)
                decrypted_text += special_char[index]
            else:
                decrypted_text += char

    return decrypted_text


def fileEncrypt(user_file):
    try:
        with open(user_file, "r") as user:
            text = user.readlines()
        if generate_pin():
            with open("encrypted.txt", "w") as output:
                output.write(encrypt(text))
    except Exception as error:
        print(f"Unexpected error has occured while reading or writing: {error}\n")


def fileDecrypt(output_file):
    try:
        with open("encrypted.txt", "r") as file:
            text = file.readlines()
        with open(output_file, "w") as output:
            output.write(decrypt(text))
    except Exception as error:
        print(f"Unexpected error has occured while reading or writing: {error}\n")


if __name__ == "__main__":
    main()