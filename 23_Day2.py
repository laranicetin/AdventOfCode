# red 12, green 13, blue 14

# part 1

possible_sum = 0
file = open("23_Day2.txt", "r")
id = 0
for x in file:
    x = x.split(":")
    res = x[1].replace(';', ' ').replace(', ', ' ').split()
    dolzina = len(res)
    #print(dolzina)
    #print(res)
    id += 1
    possible_sum += id

    for i in range(int(dolzina/2)):
        #print(res[2 * i]) # kolicina
        #print(res[2*i + 1]) # barva
        if ((int(res[2 * i]) > 12) and (res[2*i + 1] == "red")) or ((int(res[2 * i]) > 13) and (res[2*i + 1] == "green")) or ((int(res[2 * i]) > 14) and (res[2*i + 1] == "blue")):
            possible_sum -= id
            break

file.close()
print(possible_sum)

# 2282 too low
# 2522 too low

# part 2

file = open("23_Day2.txt", "r")
final_sum = 0
for x in file:
    x = x.split(":")
    res = x[1].replace(';', ' ').replace(', ', ' ').split()
    dolzina = len(res)

    sum = 0
    min_red = 0
    min_green = 0
    min_blue = 0

    for i in range(int(dolzina/2)):
        #print(res[2 * i]) # kolicina
        #print(res[2*i + 1]) # barva
        if (res[2*i + 1] == "red") and (int(res[2 * i]) > min_red):
            min_red = int(res[2 * i])
        if (res[2 * i + 1] == "green") and (int(res[2 * i]) > min_green):
            min_green = int(res[2 * i])
        if (res[2*i + 1] == "blue") and (int(res[2 * i]) > min_blue):
            min_blue = int(res[2 * i])
    skupaj = min_red * min_green * min_blue
    final_sum += skupaj
# red * green * blue
# game 1 + game 2 + ...
file.close()
print(final_sum)