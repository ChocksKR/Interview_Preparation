
def trap(self, height):
    elevation_map = height
    water = 0 #keeps track of the total water as we traverse the elevation map

    n = len(elevation_map) #number of points on the map
    if n == 0:
        return n

    #lists to store the left_max and right_max of each point in the map

    left_max = [0]*n
    right_max = [0]*n

    #default values
    left_max[0] = elevation_map[0]
    right_max[n-1] = elevation_map[n-1]

    #filling the left_max list
    for i in range(1,n):
        left_max[i] = max(left_max[i-1], elevation_map[i])

    #filling the right_max list
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], elevation_map[i])

    #calculating the amount of water
    for i in range(n):
        water += min(left_max[i],right_max[i]) - elevation_map[i]

    return water

trap([0,1,0,2,1,0,1,3,2,1,2,1])
#
#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


#The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
#
#Example:

##Input: [0,1,0,2,1,0,1,3,2,1,2,1]
#Output: 6