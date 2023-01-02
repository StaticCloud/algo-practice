def mostSongs(arr):
    # sort the array so finding the most songs is easier
    # add a two counters, one for the total minute and one for total songs
    # if the total minutes exceeds 60, return the total songs
    sortedArr = sorted(arr)

    totalSongs = 0;
    totalMinutes = 0;

    for runtime in sortedArr:
        totalMinutes = totalMinutes + runtime

        if totalMinutes >= 60:
            return totalSongs

        totalSongs += 1

someList = [2,3,46,74,52,15,13,10,5,5]
print(mostSongs(someList))