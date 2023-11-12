import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
from scipy.interpolate import griddata
import cartopy.crs as ccrs

# file = "January 1"
# file = "January 18"
# file = "February 5"
# file = "February 23"
# file = "March 11"
file = "March 31"
fh = open("./data/" + file + ".txt")

min = 10000
for line in fh:
    x = len(line.split())
    if x < min:
        min = x

fh.seek(0)

data = {}
long = []
lati = []

i = 0
for line in fh:
    y = line.split()
    if i == 0:
        j = 0
        while j < min:
            if y[j][-1] == "E":
                long.append(float(y[j][:-1]))
            else:
                long.append(360 - float(y[j][:-1]))
            j += 1
    else:
        lat = y[0]
        if lat[-1] == "N":
            latVal = float(lat[:-1])
        else:
            latVal = -float(lat[:-1])
        lati.append(latVal)

        data[latVal] = {}
        j = 1
        while j < min:
            data[latVal][long[j - 1]] = float(y[j])
            j += 1
        data[latVal][long[min - 1]] = -999
        lati.append(latVal)
    i += 1

fh.close()

long = np.array(long)
lati = np.array(lati)
longitude_grid, latitude_grid = np.meshgrid(long, lati)

values = np.array([[data[lat][lon] if data[lat][lon] != -
                  999 else 0 for lon in long] for lat in lati])

x_grid, y_grid = np.meshgrid(long, lati)

z_grid = griddata(
    (longitude_grid.ravel(), latitude_grid.ravel()),
    values.ravel(),
    (x_grid, y_grid),
    method="cubic",
)

plt.figure(figsize=(16, 12))
ax = plt.axes(projection=ccrs.PlateCarree())

colormap = plt.imshow(
    z_grid,
    extent=(long.min(), long.max(), lati.min(), lati.max()),
    origin='lower', cmap="pink_r", transform=ccrs.PlateCarree(),
    norm=LogNorm()
)

plt.colorbar(colormap, ax=ax, orientation='horizontal',
             label='Data point value')
ax.set_title('Colormap Plot')

ax.coastlines()
plt.title(
    "Colour Map of Geographical Data with Longitude and Latitude for " + file+" 2022")

plt.show()
