import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
import cartopy.crs as ccrs

dates = ["Jan1", "Jan18", "Feb5", "Feb23", "Mar11", "Mar31"]


def draw(date):
    file_path = "./Rain/" + date + ".txt"

    with open(file_path, "r") as file:
        data = {}
        longitude = []
        latitude = []

        for i in np.arange(0.125, 360.0001, 0.25):
            longitude.append(i)

        for i, line in enumerate(file):
            values = line.split()
            if i != 0:
                latitude_val = values[0]
                if latitude_val[-1] == "N":
                    lat = float(latitude_val[:-1])
                elif latitude_val[-1] == "S":
                    lat = -float(latitude_val[:-1])
                latitude.append(lat)
                data[lat] = {}
                # This if condition is for errors which might occur after removing line too long
                if "-" in values[-1] or values[-1][-1] == "E":
                    values[-1] = 0
                for col_index in range(1, len(values)):
                    data[lat][longitude[col_index - 1]] = float(values[col_index])
                    if data[lat][longitude[col_index - 1]] == -999:
                        data[lat][longitude[col_index - 1]] = 0
                # This is for filling remaining for which we dont have values
                for i in range(len(values), len(longitude) + 1):
                    data[lat][longitude[i - 1]] = 0
    longitude = np.array(longitude)
    latitude = np.array(latitude)
    values = np.array([[data[lat][lon] for lon in longitude] for lat in latitude])

    # This convers into coordinate matrix
    x_grid, y_grid = np.meshgrid(longitude, latitude)
    plt.figure(figsize=(10, 6))

    ax = plt.axes(projection=ccrs.PlateCarree())
    levels = [0.01, 0.3, 0.7, 1]  # These are iso-contour values

    contour = plt.contour(
        x_grid,
        y_grid,
        values,
        cmap="viridis",
        transform=ccrs.PlateCarree(),
        levels=levels,
    )

    # This displays the color scale
    plt.colorbar(contour, label="Values")

    ax.coastlines()
    plt.title("Contour Plot of Surface Sea Rate with Longitude and Latitude of " + date)

    plt.show(block=False)


# dates = ["Jan1", "Jan18", "Feb5", "Feb23", "Mar11", "Mar31"]

# Uncomment the following draw() lines if you want for multiple dates.
draw(dates[0])
# draw(dates[1])
# draw(dates[2])
# draw(dates[3])
# draw(dates[4])
# draw(dates[5])
plt.show()
