# file = open("cebi.txt", "r")
# print(file.read())

# file = open("cebi.txt", "w")
# file.write("Makan Dulu")
# file.close()

file = open("cebi.txt", "a")
# file.write("ini text append")
file.write("\nini text append lagi")
file.close()
