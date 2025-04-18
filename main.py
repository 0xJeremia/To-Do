import json
import os

todo_file = 'todos.json'

def load_todos():
    if os.path.exists(todo_file):
        with open(todo_file, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(todo_file, 'w') as f:
        json.dump(todos, f, indent=2)

def add_todo(task):
    todos = load_todos()
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print("Added task:", task)

def list_todos():
    todos = load_todos()
    if not todos:
        print("No tasks found.")
    for i, todo in enumerate(todos):
        status = "✔" if todo['done'] else "✘"
        print(f"{i+1}. [{status}] {todo['task']}")

def mark_done(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        todos[index]['done'] = True
        save_todos(todos)
        print("Marked as done:", todos[index]['task'])
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTODO App")
        print("1. List tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            list_todos()
        elif choice == '2':
            task = input("Enter task: ")
            add_todo(task)
        elif choice == '3':
            try:
                index = int(input("Enter task number to mark as done: ")) - 1
                mark_done(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
