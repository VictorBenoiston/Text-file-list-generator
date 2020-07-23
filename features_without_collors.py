from time import sleep



def inputInt(txt):
    """
    A function that will validate weather a number is integer, or not.
    :param txt: The text to be shown just like the standard input
    :return: A callable constant as an integer number.
    """
    while True:
        number = str(input(txt)).strip()
        if number.strip() == '' or number.isalpha():
            print(f'Invalid integer number, try again!')
        else:
            return int(number)
            break


def fileCheck(file):
    """
    It checks if the file, given as the parameter file, already exists or not.
    If there's no such file, it creates a new one, called as the same parameter name given.
    :param file: The file to be checked
    """
    try:
        file_manager = open(file, 'rt')
    except FileNotFoundError:
        file_manager = open(file, 'at+')
        print(f'{file} was successfully created!')
    else:
        file_manager.close()


def newBook(file):
    """
    Made by two basic inputs, it will be given as input the name and age, and it will add on the file given as parameter.
    :param file: The file to be worked.
    """
    print(f'New book: ')
    while True:
        name = input('Type the name: ').strip().title()
        name_validation = name.strip().replace(' ', '')
        if not name_validation.isalpha():
            print(f'Invalid name, try again!')
        else:
            break
    age = inputInt('Type the age: ')
    with open(file, 'at') as file_manager:
        file_manager.write(f'{name};{age}\n')
    print(f'Registering {name}...')
    sleep(1)
    print(f'{name} was successfully booked!')
    sleep(1)


def printList(file):
    """
    Read the file given, and print the components of it, in a formatted way.
    :param file: file to be read.
    """
    print(f'Loading list...')
    sleep(1)
    print('-' * 40)
    print(f'Booked list: '.center(40))
    print('-' * 40)
    with open(file, 'rt') as file_manager:
        for line in file_manager:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]} Years')
    sleep(1)



def mainMenu(file):
    """
    Show a menu on the screen, giving the options that you have. After you chose an option, it will unchain a distinct
    block of code, from 1 to 3.
    As shown, 1 to book a new person, 2 to show the booked list and 3 to leave.
    :param file: file to be worked.
    """
    while True:
        print('-' * 40)
        print('Main menu: '.center(40))
        print('-' * 40)
        print(f'1 - Register a new person;')
        print(f'2 - Show the booked list;')
        print(f'3 - Exit.')
        print('-' * 40)
        while True:
            cmd = inputInt('Your command: ')
            if cmd > 3:
                print(f'Invalid command, try again!')
            else:
                break
        if cmd == 1:
            newBook(file)
        if cmd == 2:
            printList(file)
        if cmd == 3:
            print(f'See you soon!')
            break

