def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Name not found."

def show_phone(args, contacts):
    name, = args
    if name in contacts:
        return contacts[name]
    else:
        return "Name not found."
    
def show_all(contacts):
    for name in contacts:
        print(f'{name:^10} {contacts[name]}')
    return

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            show_all(contacts)
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
