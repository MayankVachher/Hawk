import shapefile
import numpy as np
import matplotlib.pyplot as plt


import seaborn as sns
sns.set(color_codes=True)

sf = shapefile.Reader("kolovai_trees/Kolovai-Trees-20180108.shp")
shapes = sf.shapes()

x = []
y = []
for i in range (len(shapes)):
	x.append(shapes[i].points[0][0])
	y.append(shapes[i].points[0][1])

# Visually, we do have outliers. inspect the distribution of x and y
x_arr = np.array(x)
x_mean = np.mean(x_arr, axis=0)
x_std = np.std(x_arr, axis=0)

sns.distplot(x)

