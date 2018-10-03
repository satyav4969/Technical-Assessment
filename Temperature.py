import unittest

collection = ["1,10000,40", "1,10002,45", "1,11015,50", "2,10005,42", "2,11051,45", "2,12064,42", "2,13161,42"]


def average(interval, data):
    time = map(lambda s: int(s.split(',')[1]), data)
    temp = map(lambda s: int(s.split(',')[2]), data)
    time, temp = zip(*sorted(zip(time, temp)))
    blocks = []
    tempblock = []
    block = 0
    cur_base_time = time[0];
    blocks.append([])
    tempblock.append([])
    blocks[0].append(time[0])
    tempblock[0].append(temp[0])
    i = 1
    while i < len(time):
        if time[i] >= cur_base_time + (interval - 1):
            while time[i] > cur_base_time + interval * 2:
                blocks.append([])
                tempblock.append([])
                cur_base_time += interval
                block += 1
            blocks.append([])
            tempblock.append([])
            cur_base_time += interval
            block += 1
        blocks[block].append(time[i])
        tempblock[block].append(temp[i])
        i += 1

    empty = []
    avg = []

    j = 0
    start = blocks[0][0]
    while j < len(blocks):
        empty.append(str(start + interval * j) + " - " + str(start + (interval * (j + 1)) - 1))
        j += 1

    for b in tempblock:
        total = 0
        for n in b:
            total += n
        if len(b) == 0:
            avg.append(0)
        else:
            avg.append(total / len(b))

    k = 0
    while k < len(empty):
        t = "N/A" if avg[k] == 0 else "{0:.2f}".format(avg[k])
        print(empty[k] + ": " + t)
        k += 1

print("The Average Temperature over the time is: ")
average(1000, collection)