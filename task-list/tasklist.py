from task import Task


class Tasklist:
    def __init__(self):
        self._tasklist = []
        
        with open("tasklist.txt", "r") as f:
            for line in f:
                desc, date, time = line.strip().split(",")
                new_task = Task(desc, date, time)
                if len(self) > 0:
                    for task in self._tasklist:
                        if new_task < task:
                            self._tasklist.insert(self._tasklist.index(task), new_task)
                            break
                        if self._tasklist.index(task) == len(self)-1 and not new_task < task:
                            self._tasklist.append(new_task)
                            break
                else:
                    self._tasklist.append(new_task)

    def add_task(self, desc, date, time):
        new_task = Task(desc, date, time)
        for task in self._tasklist:
            if new_task < task:
                self._tasklist.insert(self._tasklist.index(task), new_task)
                break
            if self._tasklist.index(task) == len(self) - 1 and not new_task < task:
                self._tasklist.append(new_task)

    def mark_complete(self):
        if len(self) > 0:
            del self._tasklist[0]

    def get_current_task(self):
        return self._tasklist[0]

    def save_file(self):
        with open("tasklist.txt", 'w') as f:
            for task in self._tasklist:
                f.write(repr(task) + "\n")

    # def __getitem__(self, index):
    #     return self.tasklist[index]

    def __iter__(self):
        self._n = -1
        return self

    def __next__(self):
        self._n += 1
        if self._n >= len(self._tasklist):
            raise StopIteration
        else:
            return self._tasklist[self._n]

    def __len__(self):
        return len(self._tasklist)
    

# taskl = Tasklist()

# # while taskl._n > len(taskl):
# print(taskl.__iter__())
# taskl.__next__()

# print((len(taskl)))