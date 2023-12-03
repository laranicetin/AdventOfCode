import re
# part 1

sum = 0
file = open("23_Day1.txt", "r")
for x in file:
    line_sum = 0
    x = re.sub("[A-Za-z]", "", x)
    if len(x) == 2:
        line_sum += int(x[0] + x[0])
    elif len(x) > 2:
        line_sum += int(x[0] + x[len(x) - 2])
    else:
        break
    sum += line_sum
file.close()
print(sum)
print("--------")

# part 2

sum = 0
file = open("23_Day1.txt", "r")
for x in file:
    line_sum = 0
    x = x.replace("one", "o1e")
    x = x.replace("two", "t2o")
    x = x.replace("three", "t3e")
    x = x.replace("four", "4")
    x = x.replace("five", "5e")
    x = x.replace("six", "6")
    x = x.replace("seven", "7n")
    x = x.replace("eight", "e8t")
    x = x.replace("nine", "9e")
    x = re.sub("[A-Za-z]", "", x)

    if len(x) == 2:
        line_sum += int(x[0] + x[0])
    elif len(x) > 2:
        line_sum += int(x[0] + x[len(x) - 2])
    else:
        break
    sum += line_sum
file.close()
print(sum)