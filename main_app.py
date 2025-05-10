print("Welcome to To-Do app!")
print("---------------------")
print("Below is the code format to use the app: \nadd | show | delete | exit")

list = []

while True:

    user_action = input("Enter command:")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            var = input("\nAdd your entry: ")
            if var == "back":
                continue
            list.append(var)

        case "show":
            print("\nHere's your saved list: ")
            for items in list:
                print("{0}: {1}".format(list.index(items)+1, items))
            continue

        case "delete":
            print("\nCurrent notes: ")
            for items in list:
                print("{0}: {1}".format(list.index(items)+1, items))
            
            #ensure user input < number of notes
            try:
                var = int(input("Which note to be deleted (Select by entering the number):"))
                if 1 <= var <= len(list):
                    del list[var - 1]
                    break
                else:
                    print(f"Please enter a number between 1 and {len(list)}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

            print("\nUpdated notes: ")
            for items in list:
                print(f"{list.index(items)+1} : {items}")
            continue

        case "exit":
            break

        case _:
            print("Unknown Action -_-")

print("Bye!")
