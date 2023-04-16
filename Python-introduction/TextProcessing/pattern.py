import re

pattern = r'P/(\w{2})/(\w{9})/(\w{2})/(\d{2}\w{3}\d{4})/(\w{1})/(\d{2}\w{3}\d{4})/(\w+)/(\w{2})$'
matching_lines = []

input_str = "G*L3005/07JUNDAC/DOCS/ET/PNRL\n BG 3005 07JUN DAC 900 773 DOCS ET PNRL Y405\n 1 ABDULLAH MD M AE54 U JED 32C-F 1 M ET DOCV DOCS\n 287 ETI APP HAJ\n P/BGD/A03337108/BGD/01MAR78/M/23MAR32/ABDULLAH/MD\n CFFJDO\n 9972100131253 C01 07JUN U DACJED LFTD\n 2 ABDURRAHIM MD MR AC43 U JED 20G-F NB M ET DOCV DOCS\n 363 ETI APP HAJ\n P/BD/BX0235989/BD/17JUL1964/M/29SEP2023/ABDURRAHIM/MD\n CEWECV\n 9972100130281 C01 07JUN U DACJED LFTD"

for line in input_str.splitlines():
    match = re.search(pattern, line)
    if match:
        matching_lines.append(match.group(0))

print(matching_lines)
