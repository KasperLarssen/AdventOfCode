with open('data.txt') as data:
    lines = data.readlines()
    numberOfLines = len(lines)
    lengthOfBinaryNumber = len(lines[0])
    countOnes = [0] * (lengthOfBinaryNumber - 1)
# star 1
def solution():
    # Loop through each digit in each line, and track how many 1's occur at each index position
    for binaryNumber in lines:
        i = 0
        for number in binaryNumber:
            if number == '1':
                countOnes[i] += 1
            i += 1
    i = 0
    for count in countOnes:
        # If the amount of ones are bigger than numberOflines / 2, there are more 1's than 0's, and we can set a 1 at the given index
        if count > numberOfLines / 2:
            countOnes[i] = 1
        else:
            countOnes[i] = 0
        i += 1
    # Flipping bits for the epsilon value
    gammaBinary = ''.join(map(str, countOnes))
    epsilonBinary = gammaBinary.replace('1', '2')
    epsilonBinary = epsilonBinary.replace('0','1')
    epsilonBinary = epsilonBinary.replace('2','0')
    # Converting to decimal
    gamma = int(gammaBinary, 2)
    epsilon = int(epsilonBinary, 2)

    return gamma*epsilon
print(solution())



