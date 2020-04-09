x = [1,2,3,4]
file = open("test.txt", "w")
for item in x:
    file.write(str(item) + "\n")
file.close()