def main():
    print("hello world")
    text = "hello!@#$\""
    print(encrypt(text))


def generate_key():
    password = input("Please enter your 6-Digit pin: ")
    with open("password.key", "w") as file:
        file.write(password)


def encrypt(text):
    encrypted_text = ""
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    special_char = "!@#$%^&*()-_=+[{]}\|;:,<.>/?`~"
    reversed_alphabet= alphabet[::-1]
    reversed_special = special_char[::-1]

    for char in text:
        if char.isalpha():
            index = alphabet.index(char)
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


def decrypt(text): 
    decrypted_text = ""
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    special_char = "!@#$%^&*()-_=+[{]}\|;:,<.>/?`~"
    reversed_alphabet= alphabet[::-1]
    reversed_special = special_char[::-1]

    for char in text:
        if char.isalpha():
            index = reversed_alphabet.index(char)
            if char.islower():
                decrypted_text += alphabet[index]
            else:
                decrypted_text += alphabet[index].upper()
        elif char in special_char:
            index = reversed_special.index()
            decrypted_text += special_char[index]
        else:
            decrypted_text += char

    return decrypted_text


def fileEncrpyt(user_file, output_file):
    try:
        with open(user_file, "r") as file:
            text = file.readlines()
        with open(output_file, "w") as output:
            output.write(encrypt(text))
    except Exception as error:
        print(f"Unexpected error has occured while reading: {error}")


def fileDecrypt(user_file, output_file):
    try:
        with open(user_file, "r") as file:
            text = file.readlines()
        with open(output_file, "w") as output:
            output.write(decrypt(text))
    except Exception as error:
        print(f"Unexpected error has occured while reading: {error}")


if __name__ == "__main__":
    main()