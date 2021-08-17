# enter message to encrypt using e and n
def encrypt_message(e: int, n: int):
    return pow(int(input("Please enter message to encrypt: ")), e, n)


if __name__ == '__main__':
    while True:
        try:
            option = int(input("""1 to encrypt message
2 to exit
please choose an option:"""))
            if option == 1:
                print("encrypted Message: {}".format(
                    encrypt_message(int(input("Please enter e: ")), int(input("Please enter n: ")))))
            elif option == 2:
                break
            else:
                raise ValueError
        except ValueError:
            print("you must enter valid number:")
