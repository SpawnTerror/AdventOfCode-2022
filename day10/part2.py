# Code review

def check_signal_strength(cycle):
    return (cycle == 20) or (cycle % 40 == 20 and 0 < cycle <= 220)


def process_sprite(cycle, row, x):
    mid = cycle % 40
    # Are we about to enter a new row?
    if not mid:
        row += 1
        print()
    if mid-1 <= x <= mid+1:
        print("#", end='')
    else:
        print(".", end='')


def part_one():
    with open('day10/input.txt', 'r') as f:
        input = f.read().splitlines()

    x = 1
    cycle = 0
    signal_strength = 0

    for inst in input:
        # For both noop and addx, we always need to increment at least one cycle.
        cycle += 1
        if check_signal_strength(cycle):
            signal_strength += cycle * x
        if inst.startswith("addx"):
            # addx takes two cycles. We've already checked the cycle count after the first cycle, so add the second one here.
            cycle += 1
            if check_signal_strength(cycle):
                signal_strength += cycle * x
            x += int(inst.split()[1])
    return signal_strength


def part_two():
    with open('day10/input.txt', 'r') as f:
        input = f.read().splitlines()

    x = 1
    cycle = 0
    row = 0

    for inst in input:
        if inst == "noop":
            # noop takes one cycle.
            process_sprite(cycle, row, x)
            cycle += 1
        elif inst.startswith("addx"):
            # addx takes two cycles.
            for _ in range(2):
                process_sprite(cycle, row, x)
                cycle += 1

            x += int(inst.split()[1])


def main():
    print(part_one())
    part_two()


if __name__ == '__main__':
    main()