my_file = open('ex1_data.txt', mode='r')
print(my_file)
print(type(my_file))
line_no = 0
for line in my_file:
    if "Theodosia" in line:
        print("Found! At: ", line_no)
    line_no += 1
    print(line)

my_file.close()

nightmare = "This is excessive\n\n\n\n\n\n\n\n\n        "
print(nightmare.rstrip())
