from typing import List, Optional

id_last = 0
priorities = ("High", "Medium", "Low")
statuses = ("Pending", "In Progress", "Completed")

class Task:
    def __init__(self, title, desc, priority, status):
        global id_last
        self.id: int = id_last
        id_last += 1
        self.title: str = title
        self.desc: str = desc
        self.priority: int = priority
        self.status: int = status

    def __str__(self):
        return (f"Task ID: {self.id}, Title: {self.title}, Description: "
                f'{self.desc}, Priority: {priorities[self.priority]}, Status: '
                f'{statuses[self.status]}')


def get_priority(printable, include_empty_string=False):
    priority = input(printable)
    while priority not in priorities + (("",) if include_empty_string else ()):
        print(f'please enter valid priority out of {priorities}')
        priority = input(printable)
    if not priority: return None
    return priorities.index(priority)


def get_status(printable, include_empty_string=False):
    status = input(printable)
    while status not in statuses + (("",) if include_empty_string else ()):
        print(f'please enter valid status out of {statuses}')
        status = input(printable)
    if not status: return None
    return statuses.index(status)


class TaskManager:

    def __init__(self):
        self.tasks: List[Optional[Task]] = []

    def add_task(self):
        title = input("Enter task title:")
        description = input("Enter task description:")
        priority = get_priority('Enter task priority (High/Medium/Low):')
        status = get_status('Enter task status (Pending/In Progress/Completed):')
        self.tasks.append(Task(title, description, priority, status))

    def edit_task(self):
        tid = input("Enter task ID to edit :")
        while not (tid.isdigit() and 0 <= int(tid) < id_last and self.tasks[int(tid)] is not None):
            print(f"Enter only valid and existing task ID")
            tid = input("Enter task ID to edit :")
        tid = int(tid)
        title = input("Enter new title: (leave blank to keep existing)")
        if title:
            self.tasks[tid].title = title
        description = input("Enter new task description(leave blank to keep existing):")
        if description:
            self.tasks[tid].desc = description
        priority = get_priority('Enter new priority(leave blank to keep existing):', True)
        if priority:
            self.tasks[tid].priority = priority
        status = get_status('Enter new status (leave blank to keep existing):', True)
        if status:
            self.tasks[tid].status = status

    def delete_task(self):
        tid = input("Enter task ID to delete :")
        while not (tid.isdigit() and 0 <= int(tid) < id_last and self.tasks[int(tid)] is not None):
            print(f"Enter only valid and existing task ID")
            tid = input("Enter task ID to delete :")
        self.tasks[int(tid)] = None

    def get_task_by_id(self, tid):
        return self.tasks[tid]

    def view_all_tasks(self):
        for i in range(id_last):
            task = self.get_task_by_id(i)
            if task:
                print(task)

    def filter_tasks_by_priority(self):
        priority = get_priority("Enter priority to filter tasks (High/Medium/Low):")
        for i in range(id_last):
            task = self.get_task_by_id(i)
            if task and priority == task.priority:
                print(task)


tm = TaskManager()


def get_choice():
    while True:
        a = input("Enter your choice (1-6) :")
        if not (len(a) == 1 and '1' <= a[0] <= '6'):
            print("Invalid input! please try again.")
            continue
        return int(a)


def get_new_input():
    print("""
    1. Add task
    2. Edit task
    3. Delete task
    4. View all tasks
    5. Filter tasks by priority
    6. Exit
""")
    ch = get_choice()
    if ch == 1:
        tm.add_task()
    elif ch == 2:
        tm.edit_task()
    elif ch == 3:
        tm.delete_task()
    elif ch == 4:
        tm.view_all_tasks()
    elif ch == 5:
        tm.filter_tasks_by_priority()
    else:
        return False
    return True


while get_new_input():
    pass
