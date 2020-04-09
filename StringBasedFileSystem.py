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
