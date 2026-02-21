input_file = "ascii_input.txt"
output_file = "output_ascii.svg"

adjusted_lines = []
start_y = 50
x_val = 15
y_offset = 20

with open(input_file, "r", encoding="utf-8") as f:
  for i, line in enumerate(f):
    line = line.rstrip()
    tspan = f'<tspan x="{x_val}" y="{start_y+(i*y_offset)}">{line}</tspan>'
    adjusted_lines.append(tspan)


with open(output_file, "w") as f:
    for l in adjusted_lines:
        f.write(l + "\n")

print(f"generated svg with height of {len(adjusted_lines)} of ascii art and saved it to {output_file}")
