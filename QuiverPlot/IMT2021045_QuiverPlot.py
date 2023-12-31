# -*- coding: utf-8 -*-
"""DV_A2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JFqmeiM2i2DcmppPb-RTNMagcVEvF_IF
"""

# Data Visualization Assignment
# Name: Goutham U R
# Roll No.: IMT2021045
# Team name: Colourblinds

pip install cartopy

import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Load data from the file
file_path = "/content/zonal_23.txt"
try:
    with open(file_path, "r") as file:
        lines_zonal = file.readlines()[6:]  # Ignore the first 6 lines
except FileNotFoundError:
    print(f"The file {file_path} was not found.")
print(lines_zonal)

# Load data from the file
file_path = "/content/meridonial_23.txt"
try:
    with open(file_path, "r") as file:
        lines_meridonial = file.readlines()[6:]  # Ignore the first 6 lines
except FileNotFoundError:
    print(f"The file {file_path} was not found.")
print(lines_meridonial)

# Determine the minimum line length (excluding the header row)
min_zonal = min(len(line.strip().split()) for line in lines_zonal)
min_meri = min(len(line.strip().split()) for line in lines_meridonial)
min_len=min(min_zonal,min_meri)
print(min_len)

# Process and clean the data
cleaned_data_zonal = []
for line in lines_zonal:
    parts = line.strip().split()[:min_len]
    cleaned_line = [float(part[:-1]) if part.endswith('N') or part.endswith('E') else (-1) * float(part[:-1]) if part.endswith('S') or part.endswith('W') else float(part) for part in parts]
    cleaned_data_zonal.append(cleaned_line)

# print(cleaned_data_zonal[0:10])

cleaned_data_meri = []
for line in lines_meridonial:
    parts = line.strip().split()[:min_len]
    cleaned_line = [float(part[:-1]) if part.endswith('N') or part.endswith('E') else (-1) * float(part[:-1]) if part.endswith('S') or part.endswith('W') else float(part) for part in parts]
    cleaned_data_meri.append(cleaned_line)

# print(cleaned_data_meri[0:10])

data_zonal = np.array(cleaned_data_zonal, dtype=float)
data_meridonial = np.array(cleaned_data_meri, dtype=float)

# For a clear quiver plot make sure that the diffrence is less than 30
lat_start=120
lat_end=140
long_start=120
long_end=140


# # Extract latitudes and longitudes
latitudes = data_zonal[lat_start:lat_end, 0]
longitudes = data_zonal[0, long_start:long_end]
zonal_data = data_zonal[lat_start:lat_end, long_start:long_end]
meridonial_data = data_meridonial[lat_start:lat_end, long_start:long_end]


print(latitudes[0])
print(latitudes[-1])
print(longitudes[0])
print(longitudes[-1])

# Create a mesh grid for latitudes and longitudes
lon, lat = np.meshgrid(longitudes, latitudes)
print(lon.size)

plt.figure(figsize=(10, 8))
ax = plt.axes(projection=ccrs.PlateCarree())

ax.coastlines()
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.LAND, edgecolor='black')
ax.add_feature(cfeature.OCEAN, zorder=0)

# Convert lat/lon to map projection coordinates
x, y = ax.projection.transform_points(ccrs.PlateCarree(), lon, lat)[:2]

# Ensure U and V have the correct size by reshaping
U = zonal_data.flatten()
V = meridonial_data.flatten()


# Plot the quiver arrows
ax.quiver(lat, lon, U, V, scale=200, pivot='middle', color='red')

plt.title("Quiver Plot on World Map")
plt.show()

pip install Pillow imageio

from PIL import Image
import imageio

def create_gif(images, output_gif_path, duration=0.5):
    frames = []

    for image_path in images:
        img = Image.open(image_path)
        frames.append(img)

    imageio.mimsave(output_gif_path, frames, duration=duration)

# Example usage:
image_paths = ["/content/p19.png", "/content/p20.png", "/content/p21.png", "/content/p22.png", "/content/p23.png"]
output_gif_path = "output.gif"
create_gif(image_paths, output_gif_path)

