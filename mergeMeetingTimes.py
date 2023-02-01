def mergeMeetingTimes(arr):
    arr.sort()
    meetingTimes = []

    index = 0;

    while index < len(arr) - 1:
        currentMeeting = arr[index]
        nextMeeting = arr[index + 1]

        if currentMeeting[1] < nextMeeting[0]:
            meetingTimes.append(currentMeeting)
            index = index + 1;
        else:
            currentMeeting[1] = nextMeeting[1]
            arr.pop(index + 1)

    return arr;

print(mergeMeetingTimes([[ 5, 8 ], [ 1, 4 ], [ 6, 8 ]]))
print(mergeMeetingTimes([[ 1, 3 ], [ 2, 4 ]]))

