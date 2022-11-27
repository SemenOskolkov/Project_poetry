import getpass


def main():
    name = getpass.getuser().capitalize()

    print(f'Hello {name} you use Poetry!')

