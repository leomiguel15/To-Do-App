print("Welcome to To-Do app!")
print("Below is the code format to use the app: \nadd | show | exit")

list = []

while True:

    user_action = input("Enter command: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            var = input("Add your entry: ")
            if var == "back":
                continue
            list.append(var)

        case "show":
            print("Here's your saved list: ")
            for items in list:
                print(items)
            continue
        case "exit":
            break

print("Bye")
