

def main():
    print("hello world")


def generate_key():
    pin = input("Enter a four charecter string: ")
    with open("pinInformation.key") as file:
        file.write(pin)

def encrypt(self):
    return "hi"

def fileEncrpyt(user_file, output_file):
    try:
        with open(user_file, "r") as file:
            text = file.readlines()
    except Exception as error_input:
        print(f"Unexpected error has occured while reading: {error_input}")
    try:
        with open(output_file, "w") as out:
            out.write(text.encrypt())
    except Exception as error_output:
        print(f"Unexpected error has occured while writing: {error_output}")

    
    


    





if __name__ == "__main__":
    main()
