todos = []
 
while True:
    user_action = input("Type add or show or (q)uit: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item) 
        case 'q':
            break
        case whatever: #variable defined on the fly to catch any other input
            print("Hey you enteered an unknown command")

print("Goodbye!")