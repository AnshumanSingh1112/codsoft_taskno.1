class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the list.')

    def delete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            removed_task = self.tasks.pop(task_number)
            print(f'Task "{removed_task}" removed from the list.')
        else:
            print('Invalid task number.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks in the list.')
        else:
            print('To-Do List:')
            for idx, task in enumerate(self.tasks, start=1):
                print(f'{idx}. {task}')

def main():
    todo_list = ToDoList()
    while True:
        print('\nOptions:')
        print('1. Add Task')
        print('2. Delete Task')
        print('3. View Tasks')
        print('4. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            task = input('Enter the task: ')
            todo_
