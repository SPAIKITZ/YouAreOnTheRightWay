import time
import sys

time.sleep(2)


def print_text(text):
    for i in text:
        if i == ' ' or i == '.':
            time.sleep(0.1)
            sys.stdout.write(i)
            sys.stdout.flush()
        else:
            time.sleep(0.04)
            sys.stdout.write(i)
            sys.stdout.flush()
    time.sleep(1.5)


print('')

import time, random
import string

random_string = [''.join([random.choice(string.ascii_letters) for n in range(10)])]
# items = [chr(i) for i in range(0x30a1, 0x30ff + 1)]Nums are 11


for i in range(1, 5):
    # items.append(str(i))
    # items.append(" "*i)
    random_string.append(str(i))
    random_string.append(" " * i)


def rain(row, column):
    for i in range(row):
        s = ''
        for j in range(column):
            ri = random.randrange(len(random_string))
            s += random_string[ri]
        # print("Sup3rh@ck3r123")

        print(s)
        time.sleep(0.05)

def rain1(row, column):
    for i in range(row):
        s = ''
        for j in range(column):
            ri = random.randrange(len(random_string))
            s += random_string[ri]
        # print("Sup3rh@ck3r123")

        print(s)
        time.sleep(0.05)

def rain2(row, column):
    for i in range(row):
        s = ''
        for j in range(column):
            ri = random.randrange(len(random_string))
            s += random_string[ri]
        # print("Sup3rh@ck3r123")

        print(s)
        time.sleep(0.05)

# while True:
#     rain(10,10)
#     print_text("U are close to 2nd part of the token.\n")
#     print_text("To find it u have to go to the link on google docs!1!1!!!\n")
#     print_text("https://docs.google.com/document/d/ a ShHYrz5FMbiHE6Z4oKD_0Wr9PGFQDq3sVRXtzLLVk/edit?usp=sharing")
#     print_text("But I lost 2 numbers from the link. U have to combine it. Come on , it only 100 combinations possible))))")
#     print_text(
#         "Hint: they are around u. They are very close to you!!")while True:
#     rain(10,10)
#     print_text("U are close to 2nd part of the token.\n")
#     print_text("To find it u have to go to the link on google docs!1!1!!!\n")
#     print_text("https://docs.google.com/document/d/ a ShHYrz5FMbiHE6Z4oKD_0Wr9PGFQDq3sVRXtzLLVk/edit?usp=sharing")
#     print_text("But I lost 2 numbers from the link. U have to combine it. Come on , it only 100 combinations possible))))")
#     print_text(
#         "Hint: they are around u. They are very close to you!!")while True:
#     rain(10,10)
#     print_text("U are close to 2nd part of the token.\n")
#     print_text("To find it u have to go to the link on google docs!1!1!!!\n")
#     print_text("https://docs.google.com/document/d/ a ShHYrz5FMbiHE6Z4oKD_0Wr9PGFQDq3sVRXtzLLVk/edit?usp=sharing")
#     print_text("But I lost 2 numbers from the link. U have to combine it. Come on , it only 100 combinations possible))))")
#     print_text(
#         "Hint: they are around u. They are very close to you!!")while True:
#     rain(10,10)
#     print_text("U are close to 2nd part of the token.\n")
#     print_text("To find it u have to go to the link on google docs!1!1!!!\n")
#     print_text("https://docs.google.com/document/d/ a ShHYrz5FMbiHE6Z4oKD_0Wr9PGFQDq3sVRXtzLLVk/edit?usp=sharing")
#     print_text("But I lost 2 numbers from the link. U have to combine it. Come on , it only 100 combinations possible))))")
#     print_text(
#         "Hint: they are around u. They are very close to you!!")while True:
#     rain(10,10)
#     print_text("U are close to 2nd part of the token.\n")
#     print_text("To find it u have to go to the link on google docs!1!1!!!\n")
#     print_text("https://docs.google.com/document/d/ a ShHYrz5FMbiHE6Z4oKD_0Wr9PGFQDq3sVRXtzLLVk/edit?usp=sharing")
#     print_text("But I lost 2 numbers from the link. U have to combine it. Come on , it only 100 combinations possible))))")
#     print_text(
#         "Hint: they are around u. They are very close to you!!")while True:
#     rain(10,10)
#     print_text("U are close to 2nd part of the token.\n")
#     print_text("To find it u have to go to the link on google docs!1!1!!!\n")
#     print_text("https://docs.google.com/document/d/ a ShHYrz5FMbiHE6Z4oKD_0Wr9PGFQDq3sVRXtzLLVk/edit?usp=sharing")
#     print_text("But I lost 2 numbers from the link. U have to combine it. Come on , it only 100 combinations possible))))")
#     print_text(
#         "Hint: they are around u. They are very close to you!!")while True:
#     rain(10,10)
#     print_text("U are close to 2nd part of the token.\n")
#     print_text("To find it u have to go to the link on google docs!1!1!!!\n")
#     print_text("https://docs.google.com/document/d/ a ShHYrz5FMbiHE6Z4oKD_0Wr9PGFQDq3sVRXtzLLVk/edit?usp=sharing")
#     print_text("But I lost 2 numbers from the link. U have to combine it. Come on , it only 100 combinations possible))))")
#     print_text(
#         "Hint: they are around u. They are very close to you!!")while True:
#     rain(10,10)
#     print_text("U are close to 2nd part of the token.\n")
#     print_text("To find it u have to go to the link on google docs!1!1!!!\n")
#     print_text("https://docs.google.com/document/d/ a ShHYrz5FMbiHE6Z4oKD_0Wr9PGFQDq3sVRXtzLLVk/edit?usp=sharing")
#     print_text("But I lost 2 numbers from the link. U have to combine it. Come on , it only 100 combinations possible))))")
#     print_text(
#         "Hint: they are around u. They are very close to you!!")

while True:
    rain(30,20)
    print_text("U are close to 2nd part of the token.\n")
    print_text("To find it u have to go to the link on google docs!1!1!!!\n")
    print_text("https://docs.google.com/document/d/<>a<>ShHYrz5FMbiHE6Z4oKD_0Wr9PGFQDq3sVRXtzLLVk/edit?usp=sharing \n")
    print_text("But I lost 2 numbers from the link(it must be in <> in the link).\n U have to combine it. Come on , it only 100 combinations possible))))\n")
    print_text(
        "Hint: they are around u. They are very close to you!!\n")
    break


#
# while True:
#     rain(10,10)
#     print_text("U are close to 2nd part of the token.\n")
#     print_text("To find it u have to go to the link on google docs!1!1!!!\n")
#     print_text("https://docs.google.com/document/d/ a ShHYrz5FMbiHE6Z4oKD_0Wr9PGFQDq3sVRXtzLLVk/edit?usp=sharing")
#     print_text("But I lost 2 numbers from the link. U have to combine it. Come on , it only 100 combinations possible))))")
#     print_text(
#         "Hint: they are around u. They are very close to you!!")while True:
#     rain(10,10)
#     print_text("U are close to 2nd part of the token.\n")
#     print_text("To find it u have to go to the link on google docs!1!1!!!\n")
#     print_text("https://docs.google.com/document/d/ a ShHYrz5FMbiHE6Z4oKD_0Wr9PGFQDq3sVRXtzLLVk/edit?usp=sharing")
#     print_text("But I lost 2 numbers from the link. U have to combine it. Come on , it only 100 combinations possible))))")
#     print_text(
#         "Hint: they are around u. They are very close to you!!")while True:
#     rain(10,10)
#     print_text("U are close to 2nd part of the token.\n")
#     print_text("To find it u have to go to the link on google docs!1!1!!!\n")
#     print_text("https://docs.google.com/document/d/ a ShHYrz5FMbiHE6Z4oKD_0Wr9PGFQDq3sVRXtzLLVk/edit?usp=sharing")
#     print_text("But I lost 2 numbers from the link. U have to combine it. Come on , it only 100 combinations possible))))")
#     print_text(
#         "Hint: they are around u. They are very close to you!!")while True:
#     rain(10,10)

def rain5(row, column):
    for i in range(row):
        s = ''
        for j in range(column):
            ri = random.randrange(len(random_string))
            s += random_string[ri]
        # print("Sup3rh@ck3r123")

        print(s)
        time.sleep(0.05)

def rain6(row, column):
    for i in range(row):
        s = ''
        for j in range(column):
            ri = random.randrange(len(random_string))
            s += random_string[ri]
        # print("Sup3rh@ck3r123")

        print(s)
        time.sleep(0.05)
#     print_text("U are close to 2nd part of the token.\n")
#     print_text("To find it u have to go to the link on google docs!1!1!!!\n")
#     print_text("https://docs.google.com/document/d/ a ShHYrz5FMbiHE6Z4oKD_0Wr9PGFQDq3sVRXtzLLVk/edit?usp=sharing")
#     print_text("But I lost 2 numbers from the link. U have to combine it. Come on , it only 100 combinations possible))))")
#     print_text(
#         "Hint: they are around u. They are very close to you!!")while True:
#     rain(10,10)
#     print_text("U are close to 2nd part of the token.\n")
#     print_text("To find it u have to go to the link on google docs!1!1!!!\n")
#     print_text("https://docs.google.com/document/d/ a ShHYrz5FMbiHE6Z4oKD_0Wr9PGFQDq3sVRXtzLLVk/edit?usp=sharing")
#     print_text("But I lost 2 numbers from the link. U have to combine it. Come on , it only 100 combinations possible))))")
#     print_text(
#         "Hint: they are around u. They are very close to you!!")while True:
#     rain(10,10)
#     print_text("U are close to 2nd part of the token.\n")
#     print_text("To find it u have to go to the link on google docs!1!1!!!\n")
#     print_text("https://docs.google.com/document/d/ a ShHYrz5FMbiHE6Z4oKD_0Wr9PGFQDq3sVRXtzLLVk/edit?usp=sharing")
#     print_text("But I lost 2 numbers from the link. U have to combine it. Come on , it only 100 combinations possible))))")
#     print_text(
#         "Hint: they are around u. They are very close to you!!")while True:
#     rain(10,10)
#     print_text("U are close to 2nd part of the token.\n")
#     print_text("To find it u have to go to the link on google docs!1!1!!!\n")
#     print_text("https://docs.google.com/document/d/ a ShHYrz5FMbiHE6Z4oKD_0Wr9PGFQDq3sVRXtzLLVk/edit?usp=sharing")
#     print_text("But I lost 2 numbers from the link. U have to combine it. Come on , it only 100 combinations possible))))")
#     print_text(
#         "Hint: they are around u. They are very close to you!!")while True:
#     rain(10,10)
#     print_text("U are close to 2nd part of the token.\n")
#     print_text("To find it u have to go to the link on google docs!1!1!!!\n")
#     print_text("https://docs.google.com/document/d/ a ShHYrz5FMbiHE6Z4oKD_0Wr9PGFQDq3sVRXtzLLVk/edit?usp=sharing")
#     print_text("But I lost 2 numbers from the link. U have to combine it. Come on , it only 100 combinations possible))))")
#     print_text(
#         "Hint: they are around u. They are very close to you!!")
