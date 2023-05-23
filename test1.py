import sys


def run_boot_code(instructions):
    accumulator = 0
    pointer = 0
    visited = set()

    while True:
        if pointer in visited:
            return accumulator
        visited.add(pointer)

        if instructions[pointer].strip() == '':
            pointer += 1
            continue

        operation, argument = instructions[pointer].split()
        if operation == "acc":
            accumulator += int(argument)
            pointer += 1
        elif operation == "jmp":
            pointer += int(argument)
        elif operation == "nop":
            pointer += 1


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        instructions = [line.strip() for line in f]
        print(run_boot_code(instructions))
