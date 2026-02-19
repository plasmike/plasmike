
target_file = "../me.py"

start_x = 400
start_y = 30
line_height = 20

svg_tspans = []

with open(target_file, "r") as f:
  code_lines  = f.readlines()

for i, line in enumerate(code_lines):
  line = line.rstrip("/n")
  y = start_y + i * line_height

  stripped = line.lstrip()
  indent = line[:len(line) - len(stripped)]
  parts = stripped.split(" ", 1)
  keyword = parts[0] if parts else ""
  rest = parts[1].rstrip("\n") if len(parts) > 1 else ""

  tspan_line = ""
  if keyword:
      tspan_line += f'<tspan x="{start_x}" y="{y}" class="keyword">{indent}{keyword}</tspan>'
  if rest:
      tspan_line += f'<tspan class="class_name">{rest}</tspan>'

  svg_tspans.append(tspan_line)

svg_content = '<text font-family="monospace" font-size="16">\n' + "\n".join(svg_tspans) + "\n</text>"

with open("code_output.svg", "w") as f:
  f.write(svg_content)

print("success!")
