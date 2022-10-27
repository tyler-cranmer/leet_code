import math


def closest_restaurants(allLocations, numRestaurants):
    allLocations.sort(key = lambda x: math.sqrt(x[0]**2 + x[1]**2))
    return allLocations[:numRestaurants]

if __name__ == '__main__':
    allLocations= [[1,2],[3,4],[1,-1]]
    numRestaurants = 2
    print(closest_restaurants(allLocations, numRestaurants))