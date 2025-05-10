def validate_num(var, notes_length):
    if 1 <= var <= notes_length:
        return True
    else:
        print(f"Please enter a number between 1 and {notes_length}")
        return False

def display_notes(notes):
    print("\nCurrent notes: ")
    for index, item in enumerate(notes, start=1):
        print(f"{index}: {item}")

print("Welcome to To-Do app!")
print("---------------------")
print("Below is the code format to use the app: \nadd | show | edit | delete | exit")

notes = []

while True:
    user_action = input("Enter command: ").strip().lower()

    match user_action:
        case "add":
            var = input("\nAdd your entry: ")
            if var == "back":
                continue
            notes.append(var)

        case "show":
            display_notes(notes)

        case "edit":
            display_notes(notes)
            try:
                var = int(input("Enter the number corresponding to the note to edit: "))
                if validate_num(var, len(notes)):
                    replace = input("Enter the new note value: ")
                    notes[var - 1] = replace
                    display_notes(notes)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        case "delete":
            display_notes(notes)
            try:
                var = int(input("Which note to be deleted (Select by entering the number): "))
                if validate_num(var, len(notes)):
                    del notes[var - 1]
                    display_notes(notes)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        case "exit":
            break

        case _:
            print("Unknown Action -_-")

print("Bye!")
