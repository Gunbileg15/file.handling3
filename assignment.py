# Exercise 1
def read_line(filename, line_number):
    if line_number <= 0:
        return ""
    file = open(filename, "r")
    line = ""
    for _ in range(line_number):
        line = file.readline()
        if line == "":
            break
    file.close()
    if not line:
        return ""
    return line.rstrip("\n")

# Exercise 2
def reverse_lines(source, destination):
    file = open(source, "r")
    lines = file.readlines()
    file.close()

    file1 = open(destination, "w")
    count = 0
    for i in range(len(lines) - 1, -1, -1):
        file1.write(lines[i].strip() + "\n")
        count += 1
    file1.close()
    return count

# Exercise 3
def merge_files(first, second, destination):
    f1 = open(first, "r")
    f2 = open(second, "r")
    dest = open(destination, "w")
    
    count = 0
    for line in f1:
        dest.write(line.rstrip("\r\n") + "\n")
        count += 1
        
    for line in f2:
        dest.write(line.rstrip("\r\n") + "\n")
        count += 1
        
    f1.close()
    f2.close()
    dest.close()
    
    return count

# Exercise 4
def find_score(filename, name):
    file = open(filename, "r")
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 2 and parts[0] == name:
            file.close()
            return int(parts[1])
    file.close()
    return -1

# Exercise 5
def update_score(filename, name, new_score):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    found = False
    for i in range(len(lines)):
        parts = lines[i].strip().split(",")
        if len(parts) == 2 and parts[0] == name:
            lines[i] = name + "," + str(new_score) + "\n"
            found = True

    if found:
        file = open(filename, "w")
        for i in range(len(lines)):
            file.write(lines[i])
        file.close()
        return True

    return False
