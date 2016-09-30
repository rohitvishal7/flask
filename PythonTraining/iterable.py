# looping over a list.
>>> for i in [1, 2, 3, 4]:
...     print i,
...
1
2
3
4

# loops over its characters.
>>> for c in "python":
...     print c
...
p
y
t
h
o
n

# loops over its keys.
>>> for k in {"x": 1, "y": 2}:
...     print k
...
y
x


>>> for line in open("a.txt"):
...     print line,
...
first line
second line