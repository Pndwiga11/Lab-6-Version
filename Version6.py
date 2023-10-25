def encode(password):
    encoded = ''
    for i in range(0,len(password)):
        digit = int(password[i]) + 3
        if digit > 9:
            digit = digit % 10
        encoded += str(digit)
    return encoded

def decode(password):
    decoded = ''
    for i in range(0, len(password)):
        digit = int(password[i]) - 3
        if digit < 0:
            digit = digit + 10
        decoded += str(digit)
    return decoded

def main():

    encoded = None

    while True:
        print('Menu')
        print('------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()

        menu_selection = int(input('Please enter an option: '))
        if menu_selection == 1:
            password = input('Please enter your password to encode: ')
            encoded = encode(password)
        elif menu_selection == 2:
            decoded = decode(encoded)
            print('The enncoded password is ' + encoded + ' and the original passoword is ' + decoded + '.')
        elif menu_selection == 3:
            break

if __name__ == "__main__":
    main()
