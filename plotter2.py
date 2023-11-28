import os
import re
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Specify the directory path here
directory_path = './images'  # Change this to the path of your image directory


def extract_placeholders_and_mapping(directory):
    placeholder_mapping = {}
    sfc_placeholders = set()
    tky_placeholders = set()
    pattern = r'blend_of_(.*?)_and_(.*?)__8k__'

    for filename in os.listdir(directory):
        if filename.endswith(".png"):  # Checking if the file is a PNG file
            matches = re.findall(pattern, filename)
            if matches:
                city1, city2 = matches[0]
                sfc_placeholders.add(city1)
                tky_placeholders.add(city2)
                placeholder_mapping[filename] = (city1, city2)

    return list(sfc_placeholders), list(tky_placeholders), placeholder_mapping

# Extract placeholders and mapping
sfc_placeholders, tky_placeholders, placeholder_mapping = extract_placeholders_and_mapping(directory_path)

# Create a figure with subplots
fig, axes = plt.subplots(len(sfc_placeholders), len(tky_placeholders), figsize=(20, 20))  # Adjust figsize as necessary

# Adjust spacing and layout
plt.subplots_adjust(hspace=0.5, wspace=0.5)
fig.tight_layout()  # This will adjust spacing automatically to fit elements

# Plot each image in its corresponding subplot
for filename, (sfc, tky) in placeholder_mapping.items():
    row = sfc_placeholders.index(sfc)
    col = tky_placeholders.index(tky)
    img = mpimg.imread(os.path.join(directory_path, filename))
    axes[row, col].imshow(img)
    axes[row, col].axis('off')  # Hide axis

# Set the labels for each axis
for ax, col in zip(axes[0], tky_placeholders):
    ax.set_title(col, size='large')

for ax, row in zip(axes[:,0], sfc_placeholders):
    ax.set_ylabel(row, size='large', rotation=0, labelpad=30)  # Increase labelpad if necessary

# This will ensure that the labels are within the figure bounds
plt.subplots_adjust(left=0.15, right=0.85, top=0.95, bottom=0.05)

plt.show()