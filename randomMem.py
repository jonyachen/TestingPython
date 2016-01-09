import random


def randomMem():
    return random.randrange(0, 1000)



#   for i in range(0, len(list)):

length = 5
mem = []
for a in range(0, length):
    mem[a] = randomMem();

for c in range(0, length):
    print mem[c];