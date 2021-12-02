with open("data.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line)

#star 1
def solution():
    x = 0
    y = 0
    for line in lines:
        parsedValues = line.split()
        direction = parsedValues[0]
        value = int((parsedValues[1]))
        if(direction == "forward"):
             x += value
        elif(direction == "down"):
             y += value
        elif(direction == "up"):
             y -= value
    return y*x
print(solution())

#star 2
def solution2():
    x = 0
    y = 0
    aim = 0
    for line in lines:
        parsedValues = line.split()
        direction = parsedValues[0]
        value = int((parsedValues[1]))
        if(direction == "forward"):
             x += value
             y += aim*value
        elif(direction == "down"):
             aim += value
        elif(direction == "up"):
             aim -= value
    return y*x
print(solution2())