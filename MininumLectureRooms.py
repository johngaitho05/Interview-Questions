"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
 find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""


# A simple class that constructs a lecture object with start and end properties
class Lecture:
    def __init__(self, start, end):
        self.start = start
        self.end = end;


# Returns an index of the room where the given lecture should be assigned
def get_room_index(rooms, lecture):
    if len(rooms) == 0:
        return
    for i in range(len(rooms)):
        if noOverlap(rooms[i], lecture):
            return i

    return


# Returns True if a lecture does not overlap with any of the lectures assigned to given room else False
def noOverlap(room, lecture):
    for given_lecture in room:
        if overlapping(given_lecture, lecture):
            return False
    return True


# Checks if two lectures are overlapping
def overlapping(lecture1, lecture2):
    return (lecture1.start <= lecture2.start <= lecture1.end) or (lecture2.start <= lecture1.start <= lecture2.end)


# Takes in a list of lectures and returns the number of rooms needed
def num_rooms(lectures):
    if len(lectures) == 0:
        return
    if len(lectures) == 1:
        return 1
    lectures = [Lecture(lec[0], lec[1]) for lec in lectures]
    rooms = []
    for lecture in lectures:
        roomIndex = get_room_index(rooms, lecture)
        if roomIndex or roomIndex == 0:
            rooms[roomIndex].append(lecture)
        else:
            rooms.append([lecture])
    return len(rooms)


print(num_rooms([(30, 75), (0, 50), (60, 150), (80, 100)]))
