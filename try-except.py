from pathlib import Path

# print("Give me  two numbers, and I'll divide them.")
# print("Enter q to quit.")

# while True:
#     first_number = input("\n First Number: ")
#     if first_number == "q":
#         break

#     second_number = input("\nSecond Number: ")
#     if second_number == "q":
#         break

#     try:
#         answer = int(first_number) / int(second_number)
        
#     except ValueError:
#         print("Please enter valid numbers")

#     except ZeroDivisionError:
#         print("Sory, number can not be divided by zero.")
    
#     else:
#         print(answer)

# path = Path("guest_book.txt")

# try:
#     contents = path.read_text(encoding='utf-8')

# except FileNotFoundError:
#     print(f"Sorry, the file path {path} does not exist")

# else:
#     words = contents.split()
#     number_words = len(words)
#     print(f"The file path {path} has {number_words} words.")

def count_words(path):

    try:
        contents = path.read_text(encoding='utf-8')

    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    
    else:
        words = contents.split()
        number_words = len(words)
        print(f"The file {path} has {number_words} words.")

 
filenames = ['alix.txt', 'litle_women.txt', 'moby_dict.txt', 'wilken.txt']

for file in filenames:
    path = Path(file)
    count_words(path)