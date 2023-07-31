import sys

graph = input()
target = input()

x = graph.split(target)
print(len(x)-1)