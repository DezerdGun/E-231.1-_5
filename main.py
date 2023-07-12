#1
import datetime

a = datetime.datetime.now()
print(a)

b = datetime.datetime.now()
print(b.year)

c = datetime.datetime.now()
print(c.month)

d = datetime.datetime.now()
print(d.strftime("%W"))

e = datetime.datetime.now()
print(e.strftime("%j"))

f = datetime.datetime.now()
print(f.strftime("%d"))

g = datetime.datetime.now()
print(g.strftime("%w"))




#2
i = int(input())

if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
    print("YES")
else:
    print("NO")

