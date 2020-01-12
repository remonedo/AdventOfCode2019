
def computer(replacement1, replacement2):
    with open("Day2.txt") as file:
        text = file.read()

    items = [int(value) for value in text.split(',')]
    items[1] = replacement1
    items[2] = replacement2

    position = 0

    while True:
        command = items[position]

        if command == 99:
            break

        value1 = items[items[position + 1]]
        value2 = items[items[position + 2]]
        store_position = items[position + 3]

        if command == 1:
            items[store_position] = value1 + value2
        elif command == 2:
            items[store_position] = value1 * value2

        position += 4

    return items[0]


print(computer(12, 2))
