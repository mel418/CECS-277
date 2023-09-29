from task import Task

class Tasklist:
    def __init__(self):
        self.tasklist = []
        with open("tasklist.txt", "r") as f:
            for line in f:
                desc, date, time = line.strip().split(",")
                new_task = Task(desc, date, time)
                self.tasklist.append(new_task)
            self.tasklist.sort()

    def add_task(self, desc, date, time):
        new_task = Task(desc, date, time)
        self.tasklist.append(new_task)
        self.tasklist.sort()

    def mark_complete(self):
        if len(self) > 0:
            del self.tasklist[0]

    def save_file(self):
        with open("tasklist.txt", 'w') as f:
            for task in self.tasklist:
                f.write(repr(task) + "\n")

    def __getitem__(self, index):
        return self.tasklist[index]

    def __len__(self):
        return len(self.tasklist)