import numpy as np


def water_flow(canal, fluid):
    # function to set next volumes in river
    # if there is a flood return False
    source = 2
    fluid_next = np.zeros(len(fluid))
    fluid_next[0] = source
    fluid_next[1:] = fluid[:len(fluid)-1]
    for i in range(len(canal)):
        if canal[i] < fluid[i]:
            print("There is a flood")
            return False, canal, fluid_next
    return True, canal, fluid_next


length = 10
# length of river array represents length of the river
# values inside represent dV possible to hold
# if dV of water is bigger than dV of river
# there will be a flood
river = np.array([5 for x in range(0, length)])
water = np.zeros(length)
time = 20

for t in range(time):
    flood, river, water = water_flow(river, water)
    if not flood:
        break
else:
    print("There was no flood")
