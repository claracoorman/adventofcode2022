f = open("input.txt", "r")
lines = f.read()
list_of_lines = lines.splitlines()
f.close()
i = int(0)
b = 0
c = 0
print(list_of_lines)
for line in list_of_lines:
    try:
        a = int(line)
    except:
        if b < c:
            b = 0
            i = int(0)
        else:
            c = 0
            i = int(1)
    else:
        if i == 0:
            b = a + b
        else:
            c = a + c
print(max(b, c))
