#1
with open("txt.txt", "r") as input_file:
    with open("txt.txt", "w") as output_file:
        for line in input_file:
            words = line.split()
            long_words = [word for word in words if len(word) >= 7]
            output_file.write(" ".join(long_words) + "\n")