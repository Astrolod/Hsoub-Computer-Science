class TaskManager:
    class Task:
        def __init__(self, title, description):
            self.title = title
            self.description = description
            self.done = False

        def get_details(self):
            return f"{self.title}, {self.description}, {self.done}"


    def __init__(self):
        self.list = []

    def add_task(self, title, description):
        new_task = self.Task(title, description)
        self.list.append(new_task)

    def show_tasks(self):
        for task in self.list:
            print(f"Task title: {task.title}, description: {task.description}, Is done: {task.done}")


if __name__ == "__main__":
    to_do_list = TaskManager()

    while True:
        print("::::::::::::::::::::::\n"
                    "Welcome to TaskManger\n"
                    "::::::::::::::::::::::")
        x = int (input("to add a new task type 1,"
                    "to show a list of available tasks type 2,"
                   "to close the program type 3: "))

        if x == 1:
            to_do_list.add_task(input("enter your task title: "), input("enter your task description: "))
        elif x == 2:
            to_do_list.show_tasks()
        elif x == 3:
            break
        else:
            print("invalid input")


