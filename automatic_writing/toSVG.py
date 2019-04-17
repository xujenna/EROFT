from numpy import loadtxt
import random

with open('readings.txt') as f:
    data = f.readlines()

lines = list(loadtxt("readings.txt", delimiter="\n", unpack=False))

svgCommands = {"c": 6, "m": 2, "l": 2, "h": 1, "v": 1, "s":4, "q":4}
keys = list(svgCommands.keys())
# evenIndices = []
# oddIndicies = []

# for x in range(0, len(svgCommands) - 1):
#     if x % 2 == 0:
#         evenIndices.append(x)
#     else:
#         oddIndicies.append(x)

index = 0
lines.insert(0, 'M')
index += svgCommands['m'] + 1

while index < len(lines):
    if lines[index] % 2 == 0:
        randCommand = keys[random.randint(0, len(keys) - 1)]
        lines.insert(index, randCommand.upper())
        index += svgCommands[randCommand] + 1
    else:
        randCommand = keys[random.randint(0, len(keys) - 1)]
        lines.insert(index, randCommand)
        index += svgCommands[randCommand] + 1

with open('readings_svg.txt', 'w+') as f:
    f.write(' '.join(str(x) for x in lines))