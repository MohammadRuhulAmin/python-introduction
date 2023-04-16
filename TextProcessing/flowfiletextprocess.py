import re
import json
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets

flowFile = session.get();
inputStream = session.read(flowFile)
flowfile_content = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
input_data = flowfile_content
# Initialize an empty list to hold the passenger information
passenger_info_list = []

# Split the input data into lines
lines = input_data.strip().split("\n")

# Iterate over the lines and extract the passenger information
for line in lines:
    # Use regular expressions to extract the passenger information from lines that contain it
    match = re.match(r"^\s*(\d+)\s+(.+?)\s+(\w{2})\s+(\w{1,2}\d+)\s+(\w+)\s+(\w{3})\s+(.+)$", line)
    if match:
        passenger = {}
        passenger['number'] = match.group(1)
        passenger['name'] = match.group(2).strip()
        passenger['title'] = match.group(3)
        passenger['seat'] = match.group(4)
        passenger['status'] = match.group(5)
        passenger['destination'] = match.group(6)
        passenger['flight_info'] = match.group(7).strip()

        passenger_info_list.append(passenger)

# Convert the list of passenger information to a JSON object
passenger_info_json = json.dumps(passenger_info_list)

# Print the JSON object
print(passenger_info_json)
