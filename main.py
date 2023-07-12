import datetime

a_date_time = datetime.datetime.now()
a_time = a_date_time.time()
print(a_time)

date = datetime.datetime.today()
print(date.strftime('%Y'))
print(date.strftime('%m'))
print(date.strftime('%d'))
print(date.strftime('%A'))




#1
with open("txt.txt", "r") as input_file:
    with open("txt.txt", "w") as output_file:
        for line in input_file:
            words = line.split()
            long_words = [word for word in words if len(word) >= 7]
            output_file.write(" ".join(long_words) + "\n")
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

