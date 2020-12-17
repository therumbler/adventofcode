from functools import reduce
from urllib.request import Request, urlopen

from urllib.error import HTTPError


def load_data():
    with open("day3_input1.txt") as f:
        return f.read()


def count_trees(data, dx, dy):
    data_array_1 = data.split("\n")
    data_array = [[] for _ in range(len(data_array_1))]
    for indx, row in enumerate(data_array_1):
        data_array[indx] = [_ for _ in row]
    x = 0
    y = 0
    tree_count = 0
    while True:
        try:
            element = data_array[y][x]
            if element == "#":
                tree_count += 1
                data_array[y][x] = "X"
            elif element == ".":
                data_array[y][x] = "O"

        except IndexError:
            # print("end of data_array")
            break
        x = x + dx

        y = y + dy
        if x >= len(data_array[0]):
            x -= len(data_array[0])

    print("tree_count = ", tree_count)

    return tree_count


def load_test_data():
    return """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".strip()


def main():
    data = load_data()
    # print(data)
    # data = load_test_data()
    dx = 3
    dy = 1
    tree_counts = []
    for dx, dy in (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ):
        tree_counts.append(count_trees(data, dx, dy))

    multipled = reduce((lambda x, y: x * y), tree_counts)
    print("multipled = ", multipled)


if __name__ == "__main__":
    main()
