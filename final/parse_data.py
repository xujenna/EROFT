import csv
import requests

remove = "https://img.cryptokitties.co/0x06012c8cf97bead5deae237070f9587f8e7a266d/"

with open('mturk-results.csv', newline='') as f:

    rows = csv.reader(f, delimiter=',')
    next(rows)
    for row in rows:
        img = requests.get(row[0]).content
        if(row[1] == "Yes"):
            print("criminal")
            path = "./data/train/criminal/"
            savePath = path+row[0][len(remove):len(row[0])]
            print(savePath)
            with open(savePath, 'wb') as handler:
                handler.write(img)
        elif(row[1] == "No"):
            print("noncriminal")
            path = "./data/train/noncriminal/"
            savePath = path+row[0][len(remove):len(row[0])]
            print(savePath)
            with open(savePath, 'wb') as handler:
                handler.write(img)

