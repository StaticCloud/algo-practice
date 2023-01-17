def concertFlyer(magazine, flyer):
    # split the flyer and the magazine between spaces
    # loop through each string item in the flyer and verify if it exists in the magazine
    # if not, return false
    splitMag = magazine.split(' ')
    splitFly = flyer.split(' ')

    for word in splitFly:
        if word not in splitMag:
            return False

    return True

print(concertFlyer('Whats so amazing that keeps us stargazing', 'stargazing whats keeps us so amazing'))