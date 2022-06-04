height, width = map(int, input().split())
world = list(map(int, input().split()))

water = 0
for i in range(1, width - 1):
    lmax = max(world[:i])
    rmax = max(world[i+1:])
    target = min(lmax, rmax)

    if(world[i] < target):
        water += target - world[i]

print(water)