with open("dec1\input.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

count = 0
for val in content:
    count += int(val)

print (count)