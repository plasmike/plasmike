import re

input_file = "tspan_y_input.txt"
output_file = "output_tspans.svg"

y_offset = -10


adjusted_lines = []

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if 'y="' in line:
            # find start and end of y="num"
            start = line.find('y="') + 3
            end = line.find('"', start)
            old_y = line[start:end]

            new_y = int(old_y) + y_offset
            # replace old y with new y
            new_line = line[:start] + str(new_y) + line[end:]
            adjusted_lines.append(new_line)
        else:
            adjusted_lines.append(line)

with open(output_file, "w") as f:
    for l in adjusted_lines:
        f.write(l + "\n")

print(f"adjusted tspans saved to {output_file} with y offset {y_offset}")
