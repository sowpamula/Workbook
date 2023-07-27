def great(message):
    new_message = message.capitalize()
    print("HEY HEY")
    return new_message

user_entry = input("What greeting do you want? ")
greeting = great(user_entry)
print(greeting)

