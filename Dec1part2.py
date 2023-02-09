with open("input.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

freq = 0
freqSet = {0}
first = False
while (not first):
    for x in content:
        freq += int(x)
        if(freq in freqSet):
            print(freq)
            first = True
            break
        else:
            freqSet.add(freq)