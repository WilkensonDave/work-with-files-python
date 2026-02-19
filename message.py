from pathlib import Path

# name = input("What is your name: ").title()
# path = Path("guest.txt")
# path.write_text(name)
names = ""

while True:
    name = input("What is your name: ")
    if name == "x":
        print("end!!")
        break
    names += name.title() + "\n"

    

path = Path("guest_book.txt")
path.write_text(names)