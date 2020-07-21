from time import sleep
collors = {
    "red": '\033[31m',
    "green": '\033[32m',
    "yellow": '\033[33m',
    "purple": '\033[35m',
    "blue": '\033[34m',
    "end": '\033[m'
}


def inputInt(txt):
    """
    A function that will validate weather a number is integer, or not.
    :param txt: The text to be shown just like the standard input
    :return: A callable constant as an integer number.
    """
    while True:
        number = str(input(txt)).strip()
        if number.strip() == '' or number.isalpha():
            print(f'{collors["red"]}Invalid integer number, try again!{collors["end"]}')
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
        print(f'{collors["green"]}{file} was successfully created!{collors["end"]}')
    else:
        file_manager.close()


def newBook(file):
    """
    Made by two basic inputs, it will be given as input the name and age, and it will add on the file given as parameter.
    :param file: The file to be worked.
    """
    print(f'{collors["purple"]}New book: {collors["end"]}')
    while True:
        name = input('Type the name: ').strip().title()
        name_validation = name.strip().replace(' ', '')
        if not name_validation.isalpha():
            print(f'{collors["red"]}Invalid name, try again!{collors["end"]}')
        else:
            break
    age = inputInt('Type the age: ')
    with open(file, 'at') as file_manager:
        file_manager.write(f'{name};{age}\n')
    print(f'{collors["yellow"]}Registering {name}...{collors["end"]}')
    sleep(1)
    print(f'{collors["green"]}{name} was successfully booked!{collors["end"]}')
    sleep(1)


def printList(file):
    """
    Read the file given, and print the components of it, in a formatted way.
    :param file: file to be read.
    """
    print(f'{collors["yellow"]}Loading list...{collors["end"]}')
    sleep(1)
    print('-' * 40)
    print(f'{collors["green"]}Booked list: {collors["end"]}'.center(40))
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
        print(f'{collors["yellow"]}1{collors["end"]} - {collors["blue"]}Register a new person;{collors["end"]}')
        print(f'{collors["yellow"]}2{collors["end"]} - {collors["blue"]}Show the booked list;{collors["end"]}')
        print(f'{collors["yellow"]}3{collors["end"]} - {collors["blue"]}Exit.{collors["end"]}')
        print('-' * 40)
        while True:
            cmd = inputInt('Your command: ')
            if cmd > 3:
                print(f'{collors["red"]}Invalid command, try again!{collors["end"]}')
            else:
                break
        if cmd == 1:
            newBook(file)
        if cmd == 2:
            printList(file)
        if cmd == 3:
            print(f'{collors["green"]}See you soon!{collors["end"]}')
            break
