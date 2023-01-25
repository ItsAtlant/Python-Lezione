x = set()
v = "AAABBCCDDEEFFFGF"
for i in v:
    x.add(i)

print(x)
v = set()
v = {2,4,1,"A","B","W"}
print(x.intersection(v))

v.update(x)
print(v)