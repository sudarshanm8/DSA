# import os

# class TodoList:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)
#         print(f'Task "{task}" added to the to-do list.')

#     def complete_task(self):
#         if not self.tasks:
#             print("No tasks in the to-do list.")
#         else:
#             completed_task = self.tasks.pop()
#             print(f'Task "{completed_task}" marked as completed.')

#     def display_tasks(self):
#         if not self.tasks:
#             print("No tasks in the to-do list.")
#         else:
#             print("To-Do List:")
#             for task in reversed(self.tasks):
#                 print(f'- {task}')

#     def save_to_file(self, filename='todo_list.txt'):
#         with open(filename, 'w') as file:
#             for task in self.tasks:
#                 file.write(f"{task}\n")
#         print(f'To-do list saved to {filename}.')

#     def load_from_file(self, filename='todo_list.txt'):
#         if os.path.exists(filename):
#             with open(filename, 'r') as file:
#                 self.tasks = [line.strip() for line in file.readlines()]
#             print(f'To-do list loaded from {filename}.')
#         else:
#             print(f'File {filename} not found.')

# def main():
#     todo_list = TodoList()

#     while True:
#         print("\nTo-Do List Menu:")
#         print("1. Add Task")
#         print("2. Complete Task")
#         print("3. Display Tasks")
#         print("4. Save To-Do List to File")
#         print("5. Load To-Do List from File")
#         print("6. Quit")

#         choice = input("Enter your choice (1-6): ")

#         if choice == '1':
#             task = input("Enter the task: ")
#             todo_list.add_task(task)
#         elif choice == '2':
#             todo_list.complete_task()
#         elif choice == '3':
#             todo_list.display_tasks()
#         elif choice == '4':
#             filename = input("Enter the filename to save to (default: todo_list.txt): ")
#             todo_list.save_to_file(filename)
#         elif choice == '5':
#             filename = input("Enter the filename to load from (default: todo_list.txt): ")
#             todo_list.load_from_file(filename)
#         elif choice == '6':
#             print("Exiting the program.")
#             break
#         else:
#             print("Invalid choice. Please enter a number from 1 to 6.")

# if __name__ == "__main__":
#     main()
import os

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the to-do list.')

    def remove_task(self):
        if not self.tasks:
            print('To-do list is empty. No task to remove.')
        else:
            removed_task = self.tasks.pop()
            print(f'Task "{removed_task}" removed from the to-do list.')

    def display_list(self):
        if not self.tasks:
            print('To-do list is empty.')
        else:
            print('To-do list:')
            for task in reversed(self.tasks):
                print(f'- {task}')

    def save_to_file(self, filename='todolist.txt'):
        with open(filename, 'w') as file:
            for task in reversed(self.tasks):
                file.write(f'{task}\n')
        print(f'To-do list saved to {filename}.')

    def load_from_file(self, filename='todolist.txt'):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                lines = file.readlines()
                self.tasks = [line.strip() for line in reversed(lines)]
            print(f'To-do list loaded from {filename}.')
        else:
            print(f'File {filename} not found. Creating a new to-do list.')

# Main program
todo_list = ToDoList()

while True:
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display To-Do List")
    print("4. Save To-Do List to File")
    print("5. Load To-Do List from File")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        task = input("Enter the task: ")
        todo_list.add_task(task)
    elif choice == '2':
        todo_list.remove_task()
    elif choice == '3':
        todo_list.display_list()
    elif choice == '4':
        filename = input("Enter the filename to save to (default: todolist.txt): ")
        todo_list.save_to_file(filename)
    elif choice == '5':
        filename = input("Enter the filename to load from (default: todolist.txt): ")
        todo_list.load_from_file(filename)
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
