"""
This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty
second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file
file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system.
For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and
its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path
to a file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
"""


def find_longest_path(s):
    i = j = 0
    tabs = 0
    paths = []
    while j < len(s):
        if s[j] == '\n':
            if '.' in s[i:j]:
                index = i - (tabs + 1)
                paths.append(find_path(s, index, tabs, j-i))
        if s[j] == '\t':
            i = j
            tabs = 0
            while s[i] == '\t':
                tabs += 1
                i += 1
            j = i
        j += 1

    if '.' in s[i:j]:
        index = i - (tabs + 1)
        paths.append(find_path(s, index, tabs, j - i))
    return max(paths) if paths else 0


def find_path(s, index, tabs, file_length):
    i = j = index
    total = file_length
    count = 0
    while j >= 0:
        if s[j] == '\t':
            temp = 0
            while s[j] == '\t':
                temp += 1
                j -= 1

            if temp == tabs-1 and '.' not in s[j:i]:
                total += count
                tabs -= 1
            i = j
            count = 0
        count += 1
        j -= 1

    total += count

    return total


dir_string = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(find_longest_path(dir_string))