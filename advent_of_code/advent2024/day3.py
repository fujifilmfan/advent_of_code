import re


memory = []
with open("day3_input.txt") as f:
    for line in f:
        line.rstrip("\n")
        memory.append(line)

mem_str = "".join(memory)

# mul_regex = re.compile(r"(mul\([0-9]{1,3},[0-9]{1,3}\))")
int_regex = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")

total = 0
for match in re.finditer(int_regex, mem_str):
    num1, num2 = match.groups()
    int1, int2 = int(num1), int(num2)

    total += int1 * int2

print(total)  # 178538786 <-- correct

do_regex = re.compile(r"do\(\)")
dont_regex = re.compile(r"don't\(\)")

instructions = {}
for match in re.finditer(do_regex, mem_str):
    instructions[match.start()] = "do"
for match in re.finditer(dont_regex, mem_str):
    instructions[match.start()] = "dont"
for match in int_regex.finditer(mem_str):
    num1, num2 = match.groups()
    int1, int2 = int(num1), int(num2)
    instructions[match.start()] = int1 * int2

total = 0
multiply = True
for k in sorted(instructions.keys()):
    if instructions[k] == "do":
        multiply = True
    elif instructions[k] == "dont":
        multiply = False
    else:
        if multiply:
            total += instructions[k]

print(total)  # 102467299 <-- correct
