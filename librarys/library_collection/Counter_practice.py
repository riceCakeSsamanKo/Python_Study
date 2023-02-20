from collections import Counter

color = ["red", "blue", "green", "red", "red", "blue"]
counter = Counter(color)

print(counter)

countOfRed = counter["red"]
countOfBlue = counter["blue"]
countOfGreen = counter["green"]

print("red="+str(countOfRed),
      "blue="+str(countOfBlue),
      "green="+str(countOfGreen))