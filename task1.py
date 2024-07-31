tasks = []

def add_task(description):
    task = {
        'id': len(tasks) + 1,
        'description': description,
        'status': 'incomplete'
    }
    tasks.append(task)
    print(f"Task added: {task}")

def update_task(task_id, new_description):
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            print(f"Task updated: {task}")
            return
    print("Task not found.")

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    print(f"Task {task_id} deleted.")

def view_tasks():
    for task in tasks:
        print(task)

def mark_task_completed(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'completed'
            print(f"Task completed: {task}")
            return
    print("Task not found.")

# Example usage
add_task("Buy groceries")
add_task("Finish project")
view_tasks()
update_task(1, "Buy groceries and cook dinner")
mark_task_completed(2)
view_tasks()
delete_task(1)
view_tasks()
