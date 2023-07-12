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