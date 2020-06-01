class TaskQueue:
    def __init__(self, name=None):
        if name is None:
            self.name = 'noname'
        else:
            self.name = name
        self.task_list = []
        self.index = 0

    def add_task(self, t):
        #print("Add: {}".format(type(t)))
        self.task_list.append(t)

    def run_next(self):
        if self.index >= len(self.task_list):
            return 2

        #print(type(self.task_list[self.index]))
        rval = self.task_list[self.index].run()
        self.index += 1
        return rval

    def wrap_index(self):
        self.index = 0
