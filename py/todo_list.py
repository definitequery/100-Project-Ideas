from pickle import load, dump

def main():
  while True:
    print("== TO-DO LIST ===")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Exit")
    choice = input('\nChoice: ')
    if choice == '4':
      print('Exiting...')
      break
    elif choice == '1':
      add_task()
    elif choice == '2':
      show_tasks()
    elif choice == '3':
      remove_task()
    else:
      print('Invalid option selected. Please select a valid option.\n')

def add_task():
  user_input = input('Enter task: ')
  if user_input:
    task = f"{user_input}"
    tasks.append(task)
    print('\nTask added!\n')
  else:
    print('Task cannot be empty. Please enter a task.\n')

def show_tasks():
  print('Your tasks:')
  for i, n in enumerate(tasks):
    print(f"{i + 1}. {n}")
  print()

def remove_task():
  try:
    task_number = int(input('Enter task number to remove: '))
    if task_number > 0 and task_number <= len(tasks):
      tasks.remove(tasks[task_number - 1])
      print('Task removed!\n')
    else:
      print('Task not found. Please enter a valid task number.\n')
  except ValueError:
    print('Invalid input. Please enter a valid task number.\n')

if __name__ == "__main__":
  try:
    with open('tasks.pkl', 'rb') as f:
      tasks = load(f)
  except FileNotFoundError:
    tasks = []
  finally:
    main()
    with open('tasks.pkl', 'wb') as f:
      dump(tasks, f)