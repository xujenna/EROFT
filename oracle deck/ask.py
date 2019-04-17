import os
import json
import random
import time

input("For what do you need clarity? ")

with open("./poetry.json", "r") as f:
    poetry = json.load(f)

randOne = random.randint(0, len(poetry)-1)
poet = poetry[randOne]
randTwo = random.randint(0, len(poet['poems'])-1)
poem = poet['poems'][randTwo]

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(str(randOne) +","+ str(randTwo))

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
time.sleep(1.5)

print(poet['symbol'].upper())
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
time.sleep(1.75)

print(poem['title'])
print("by " + poet['poet'])
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
time.sleep(1.75)

for line in poem['text']:
    print(line)
    time.sleep(1.3)