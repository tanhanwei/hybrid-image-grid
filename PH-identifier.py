import os
import re

def extract_placeholders(directory):
    sfc_placeholders = set()
    tky_placeholders = set()
    pattern = r'blend_of_(.*?)_and_(.*?)__8k__'

    for filename in os.listdir(directory):
        if filename.endswith(".png"):  # Checking if the file is a PNG file
            matches = re.findall(pattern, filename)
            if matches:
                city1, city2 = matches[0]
                # Assuming city1 is always SFC and city2 is always TKY
                sfc_placeholders.add(city1)
                tky_placeholders.add(city2)

    return list(sfc_placeholders), list(tky_placeholders)

# Specify the directory path here
directory_path = './images'

# Extract placeholders
sfc_placeholders, tky_placeholders = extract_placeholders(directory_path)

# Print the lists of unique placeholders for each city
print(len(sfc_placeholders))
print("SFC Placeholders:", sfc_placeholders)
print(len(tky_placeholders))
print("TKY Placeholders:", tky_placeholders)
