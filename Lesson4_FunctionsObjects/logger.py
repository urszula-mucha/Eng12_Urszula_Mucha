class logger:
    def __init__(self):
        self.log = []

    def add(self, msg):
        self.log.append(msg)

    def print_logs(self):
        print("\n".join(self.log))