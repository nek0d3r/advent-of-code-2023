def part1(filename, red, green, blue):
    sum = 0
    with open(filename) as f:
        for line in f.readlines():
            gameId = int(line.split(":")[0].strip().split(" ")[1])
            games = line.split(":")[1].strip().split(";")
            possible = True
            for game in games:
                sets = game.strip().split(",")
                for set in sets:
                    cubes = set.strip().split(" ")
                    if (cubes[1] == "red" and int(cubes[0]) > red) or \
                       (cubes[1] == "green" and int(cubes[0]) > green) or \
                       (cubes[1] == "blue" and int(cubes[0]) > blue):
                        print(f"game id: {gameId}, cube type: {cubes[1]}, amount: {cubes[0]}")
                        possible = False
            if possible:
                sum += gameId
    print(f"Sum of possible game IDs: {sum}")

def part2(filename):
    sum = 0
    with open(filename) as f:
        for line in f.readlines():
            gameId = int(line.split(":")[0].strip().split(" ")[1])
            games = line.split(":")[1].strip().split(";")
            red = 0
            blue = 0
            green = 0
            for game in games:
                sets = game.strip().split(",")
                for set in sets:
                    cubes = set.strip().split(" ")
                    if (cubes[1] == "red" and int(cubes[0]) > red):
                        red = int(cubes[0])
                    if (cubes[1] == "green" and int(cubes[0]) > green):
                        green = int(cubes[0])
                    if (cubes[1] == "blue" and int(cubes[0]) > blue):
                        blue = int(cubes[0])
            print(f"Game {gameId} power: {red} red + {blue} blue + {green} green = {red + green + blue}")
            sum += red * green * blue
    print(f"Sum of power of game sets: {sum}")

part2("input.txt")