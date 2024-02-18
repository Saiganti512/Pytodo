import sys
import json
from datetime import datetime

class Task:
    def __init__(self, title, priority, due_date=None):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            'title': self.title,
            'priority': self.priority,
            'due_date': self.due_date,
            'completed': self.completed
        }

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

def display_tasks(tasks):
    for i, task in enumerate(tasks, 1):
        status = '[x]' if task['completed'] else '[ ]'
        print(f'{i}. {status} {task["title"]} ({task["priority"]}) {task["due_date"]}')

def add_task(tasks):
    title = input('Enter task title: ')
    priority = input('Enter task priority (high, medium, low): ')
    due_date = input('Enter task due date (YYYY-MM-DD): ')
    task = Task(title, priority, due_date)
    tasks.append(task.to_dict())
    save_tasks(tasks)

def remove_task(tasks):
    display_tasks(tasks)
    try:
        num = int(input('Enter task number to remove: '))
        del tasks[num-1]
        save_tasks(tasks)
    except IndexError:
        print('Invalid task number.')

def complete_task(tasks):
    display_tasks(tasks)
    try:
        num = int(input('Enter task number to mark as completed: '))
        tasks[num-1]['completed'] = True
        save_tasks(tasks)
    except IndexError:
        print('Invalid task number.')

def main():
    tasks = load_tasks()
    while True:
        print('\nTo-Do List\n--------------------')
        print('1. Add task')
        print('2. Remove task')
        print('3. Complete task')
        print('4. Quit')
        print('Yours To-Do List Needs To Be Focused On You')
        try:
            choice = int(input('Enter your choice: '))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                remove_task(tasks)
            elif choice == 3:
                complete_task(tasks)
            elif choice == 4:
                sys.exit(0)
            else:
                print('Invalid choice. Please try again.')
        except ValueError:
            print('Invalid input. Please try again.')

if __name__ == '__main__':
    main()
