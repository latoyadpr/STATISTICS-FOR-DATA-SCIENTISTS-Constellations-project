# Import internal library
import codecademylib3

# 1
# Import libraries and modules
# Import matplotlib

# Import 3D visualization library


# 2
# View given x,y,z coordinates
x = [-0.41, 0.57, 0.07, 0.00, -0.29, -0.32,-0.50,-0.23, -0.23]
y = [4.12, 7.71, 2.36, 9.10, 13.35, 8.13, 7.19, 13.25,13.43]
z = [2.06, 0.84, 1.56, 2.07, 2.36, 1.72, 0.66, 1.25,1.38]

# 3
# Create a figure

# Add your subplot


# Create a scatter plot


# 4
# Create a figure

# Add your subplot


# Create a scatter plot


# Challenge
# Create a night sky scatter plot
# Create a figure

# Add your subplot

# Change color of plot background


# Create a scatter plot with black background


# Create a figure

# Add your subplot

# Change color of plot background


# Create a scatter plot with black background


# Create a figure

# Add your subplot

# Change color of plot background


# Create a scatter plot with black background

import matplotlib.pyplot as plt

# Create a figure
fig = plt.figure()

# Add a subplot
ax = fig.add_subplot(1, 1, 1)

# Create a scatter plot
ax.scatter(x, y)

# Render the visualization
plt.show()


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure for the 3D plot
fig_3d = plt.figure()

# Add a 3D subplot
ax_3d = fig_3d.add_subplot(1, 1, 1, projection='3d')

# Create a 3D scatter plot
ax_3d.scatter(x, y, z)

# Render the visualization
plt.show()


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure for the 3D plot
fig_3d = plt.figure()

# Add a 3D subplot
ax_3d = fig_3d.add_subplot(1, 1, 1, projection='3d')

# Change the background color
ax_3d.set_facecolor('black')

# Create a 3D scatter plot with white stars
ax_3d.scatter(x, y, z, color='white')

# Render the visualization
plt.show()
