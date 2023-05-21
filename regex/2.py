import re
import json

string = "/F/SUMA/MRS/MUMAYRA/HAQUE/A01071074"
split_string = string.split("/")
print(split_string)
if len(split_string) > 2:
    substring = "/".join(split_string[2:-1])
    print(substring)