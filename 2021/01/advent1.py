from window_slider import Slider
import numpy
import sys
#star 1
with open("data.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(int(line))

def solution():
    count = 0
    currentline = sys.maxsize
    for line in lines:
        if line > currentline:
            count += 1
        currentline = line
    return count

print(solution())
#star 2 
list = numpy.array(lines)

def solution2():
    #make slider array
    valuelist = []
    bucket_size = 3
    overlap_count = 2
    slider = Slider(bucket_size,overlap_count)
    slider.fit(list)
    while True:
        window_data = slider.slide()
        valuelist.append(window_data)
        if slider.reached_end_of_list(): break
    #make new array, with sum of individual slider array
    numberlist = []
    for item in valuelist:
        if item.size == 3:
            numberlist.append((item[0]+item[1]+item[2]))
    #count as in solution 1
    count = 0        
    currentItem = sys.maxsize
    for item in numberlist:
        if item > currentItem:
            count += 1
        currentItem = item
    return count

print(solution2())