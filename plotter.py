import os
import re
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def extract_placeholders(directory):
    sfc_placeholders = set()
    tky_placeholders = set()
    pattern = r'blend_of_(.*?)_and_(.*?)__8k__'

    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            matches = re.findall(pattern, filename)
            if matches:
                city1, city2 = matches[0]
                sfc_placeholders.add(city1)
                tky_placeholders.add(city2)

    return list(sfc_placeholders), list(tky_placeholders)

def create_image_grid(directory, sfc_placeholders, tky_placeholders):
    print("X-axis (TKY) placeholders:", tky_placeholders)
    print("Y-axis (SFC) placeholders:", sfc_placeholders)

    fig, axes = plt.subplots(len(sfc_placeholders), len(tky_placeholders), figsize=(20, 20), dpi=100)
    fig.subplots_adjust(left=0.25, right=0.95, bottom=0.1, top=0.9)

    for i, sfc in enumerate(sfc_placeholders):
        for j, tky in enumerate(tky_placeholders):
            filename = f'street_level_view_of_an_ultra_detailed_blend_of_{sfc}_and_{tky}__8k__highly_detailed__cinematic__intricate_details__epic__masterpiece__wide_ang.png'
            filepath = os.path.join(directory, filename)
            if os.path.exists(filepath):
                img = mpimg.imread(filepath)
                axes[i, j].imshow(img)
            axes[i, j].axis('off')

    for j, tky in enumerate(tky_placeholders):
        axes[0, j].set_title(tky, size='medium', pad=20)

    for i, ax in enumerate(axes[:, 0]):
        ax.set_ylabel(sfc_placeholders[i], size='medium', labelpad=40)

    fig.tight_layout(pad=3.0)
    plt.show()

    fig.savefig('grid_plot.png')

# Specify the directory path
directory_path = './images'

# Extract placeholders
sfc_placeholders, tky_placeholders = extract_placeholders(directory_path)

# Create and show the image grid
create_image_grid(directory_path, sfc_placeholders, tky_placeholders)
