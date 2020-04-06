"""
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""
from distutils.command.install_data import install_data


class Log:
    def __init__(self, max_size):
        self.size = 0
        self.max_size = max_size
        self.items = [None] * max_size
        self.last = -1

    def record(self, record_id):
        index = (self.last + 1) % self.max_size
        self.items[index] = record_id
        self.last = index

    def get_last(self, i):
        if i not in range(1, self.max_size+1):
            raise ValueError("i must be between 1 and " + str(self.max_size))
        index = (self.max_size + (self.last - (i - 1))) % self.max_size
        return self.items[index]


log1 = Log(5)
records = [1, 2, 3, 4, 5, 6, 7, 8]
for record in records:
    log1.record(record)
print(log1.items)
print(log1.get_last(5))