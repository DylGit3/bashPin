import sys

def main():
    print("Type the number of the desired choice: ")
    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        user_choice = input("Option: ")
        if user_choice == "1" or user_choice == "2":
            break
        elif user_choice == "3":
            sys.exit()
        else:
            print(f"{user_choice} is not a valid option.")

    if user_choice == "1":
        encrypted_file = input("Please input the name of the text file that you would like to encrypt (include \".txt\"): ")
        fileEncrypt(encrypted_file)
    elif user_choice == "2":
        decrypted_file = input("Please input the name of the text file that you would like to decrypt to (include \".txt\"): ")
        if verification_pin():
            fileDecrypt(decrypted_file)
        else:
            print("Password does not match")


def generate_pin():
    password = input("Please create your 6-Digit pin: ")
    if password.isnumeric() and len(password) == 6:
        try:
            with open("password.key", "w") as file:
                file.write(password)
        except Exception as error:
            print(f"Unexpected error has occured while reading or writing: {error}")
    else:
        print("Password does not meet qualifications, retry")


def verification_pin():
    password = input("Please enter your 6-digit pin:")
    if password.isnumeric() and len(password) == 6:
        try:
            with open("password.key", "r") as check:
                check.readline().strip() == password
                return True
        except Exception as error:
            print(f"Unexpected error has occured while reading or writing: {error}")
    else:
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
        with open("encrypted.txt", "w") as output:
            output.write(encrypt(text))
            generate_pin()
    except Exception as error:
        print(f"Unexpected error has occured while reading or writing: {error}")



def fileDecrypt(output_file):
    try:
        with open("encrypted.txt", "r") as file:
            text = file.readlines()
        with open(output_file, "w") as output:
            output.write(decrypt(text))
    except Exception as error:
        print(f"Unexpected error has occured while reading or writing: {error}")


if __name__ == "__main__":
    main()