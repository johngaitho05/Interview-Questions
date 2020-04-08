from Data_Structures.Heap.Heap import MaxHeap


class EmptyQueueError(Exception):
    pass


class PriorityQueue:
    def __init__(self):
        self.items = MaxHeap()

    def is_empty(self):
        return self.items.display() == []

    def size(self):
        return len(self.items.display())

    def enqueue(self, folder, data_priority):
        folder.priority = 1000-folder.priority
        self.items.insert(folder)

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        return self.items.delete_root()

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        return self.items.display()[0]

    def display(self):
        return [item for item in self.items.display()]


class File:
    def __init__(self, start, end, tabs):
        self.start_index = start
        self.end_index = end
        self.length = (end - start)
        self.tabs = tabs


class Dir:
    def __init__(self, start, end, tabs, length):
        self.start_index = start
        self.end_index = end
        self.length = length
        self.tabs = tabs
        self.priority = tabs


def get_dirs_and_files(s):
    files = []
    dirs = PriorityQueue()
    start = end = tabs = 0

    while end < len(s):
        if s[end] == '\n':
            if '.' not in s[start:end]:
                new_dir = Dir(start, len(s), tabs, (end - start))
                dirs.enqueue(new_dir, tabs)
            else:
                new_file = File(start, end, tabs)
                files.append(new_file)
        elif s[end] == '\t':
            start = end
            tabs = 0
            while s[start] == '\t':
                start += 1
                tabs += 1
            end = start
        end += 1

    if '.' not in s[start:len(s)]:
        new_dir = Dir(start, len(s), tabs, (end - start))
        dirs.enqueue(new_dir, tabs)
    else:
        new_file = File(start, len(s), tabs)
        files.append(new_file)

    return {'files': files, 'dirs': dirs}


def find_largest_path(s):
    dirs_and_files = get_dirs_and_files(s)
    dirs = dirs_and_files['dirs']
    files = dirs_and_files['files']
    if not dirs:
        raise ValueError("Invalid String")
    root_dir = dirs.dequeue()
    return helper(root_dir, dirs, files)


def helper(current_dir, other_dirs, files):
    current_dir_files = [file for file in files if file.tabs ==
                         current_dir.tabs + 1 and file.end_index <= current_dir.end_index]

    current_dir_subdirs = []
    while not other_dirs.is_empty():
        if other_dirs.peek().tabs == current_dir.tabs + 1:
            new_subdir = other_dirs.dequeue()
            current_dir_subdirs.append(new_subdir)
        else:
            break

    if not current_dir_files and not current_dir_subdirs:
        return 0
    if not current_dir_files:
        result = max([helper(subdir, other_dirs, files) for subdir in current_dir_subdirs])
    elif not current_dir_subdirs:
        result = max(file.length for file in current_dir_files)
    else:
        result = max(max([helper(subdir, other_dirs, files) for subdir in current_dir_subdirs]),
                     max(file.length for file in current_dir_files))
    if result != 0:
        return current_dir.length + result + 1

    return 0


dir_string = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
print(find_largest_path(dir_string))
