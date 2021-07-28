import os
import sys
import data
import settings
from models.book import Book


DATA = data.load_from_path(settings.FILE_NAME)


def clear_screen():
    if sys.platform != 'linux':
        os.system("cls") # Windows
    else:
        os.system("clear") # Linux


def home_page():
    while True:
        clear_screen()

        print("\n========== Library Management ==========\n")
        print("")
        print("1)\tNew book")
        print("2)\tAll books")
        print("3)\tExit")
        print("")

        num = input("Enter number: #").strip()
        try:
            num = int(num)

            if num == 1:
                new_book()
            elif num == 2:
                all_books()
            elif num == 3:
                break
            else:
                continue
        except:
            continue
        break
    return num


def new_book():
    while True:
        clear_screen()

        print("\n---------- New book ----------\n")
        print("")
        name = input("Name:  ")
        cat = input("Category:  ")
        about = input("About:  ")
        print("")

        print("1)\tSubmit")
        print("2)\tCancel")
        
        print("")
        num = input("Enter number: #").strip()
        try:
            num = int(num)
            if num == 1:
                b = Book(name=name, category=cat, about=about)
                b.save(DATA)
                data.save_to_path(data=DATA, path=settings.FILE_NAME)
            break
        except:
            break
    home_page()


def all_books():
    clear_screen()

    print("\n---------- Book list ----------\n")
    print("")

    if len(DATA) == 0:
        print("No book!\n")
    else:
        i = 1
        for book in DATA:
            print("*"*20)
            print(f"#{i}")
            print(str(book))
            i += 1

    print("")
    print("*"*20)
    input("Press enter to get back...")
    home_page()


if __name__ == "__main__":
    home_page()