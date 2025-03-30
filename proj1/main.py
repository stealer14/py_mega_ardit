#Input to get activity from user by displaying a prompt.
# Prmpt can be saved into variable and used in input function.
prompt = "Enter a todo: "

todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.lower()

    match user_action:
        case 'add':
            todo = input("Enter a todo activtiy: ")
            todos.append(todo)

        case 'show':
            index = 1
            for index, item in enumerate(todos):
                item = item.title()
                print(index, '-', item)

        case 'edit': #specify the index of the item to edit
            number = int(input("Number of todo to edit: "))

            #Update index number to adjust for 0 based index
            number = number - 1
            print("Current task for edit: ", todos[number])
            #replace task and update list
            
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
            print("Updated to do list:", todos)

        case 'exit':
            break

print("Bye")