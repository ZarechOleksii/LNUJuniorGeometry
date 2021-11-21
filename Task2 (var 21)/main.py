import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


def bernstein(number, current, parametric):
    binomial = math.factorial(number) / (math.factorial(current) * math.factorial(number - current))
    return binomial * math.pow(parametric, current) * math.pow((1 - parametric), (number - current))


def bezier_surface_double(points, points2, axes3d, axes1, axes2, axes3, color_line, color_line2, color_surface):
    x1 = np.array([[q[0] for q in row] for row in points])
    y1 = np.array([[q[1] for q in row] for row in points])
    z1 = np.array([[q[2] for q in row] for row in points])
    x2 = np.array([[q[0] for q in row] for row in points2])
    y2 = np.array([[q[1] for q in row] for row in points2])
    z2 = np.array([[q[2] for q in row] for row in points2])

    xes = []
    yes = []
    zes = []
    now_x = 0
    now_y = 0
    now_z = 0

    for u in np.arange(0, 1.05, 0.05):
        xes.append([])
        yes.append([])
        zes.append([])
        for v in np.arange(0, 1.05, 0.05):
            for i in range(0, len(points)):
                for j in range(0, len(points[i])):
                    now_x += bernstein(len(points) - 1, i, u) \
                        * bernstein(len(points[i]) - 1, j, v) * points[i][j][0]
                    now_y += bernstein(len(points) - 1, i, u)\
                        * bernstein(len(points[i]) - 1, j, v) * points[i][j][1]
                    now_z += bernstein(len(points) - 1, i, u) \
                        * bernstein(len(points[i]) - 1, j, v) * points[i][j][2]
            xes[-1].append(round(now_x, 2))
            yes[-1].append(round(now_y, 2))
            zes[-1].append(round(now_z, 2))
            now_x = 0
            now_y = 0
            now_z = 0
    for u in np.arange(0, 1.05, 0.05):
        xes.append([])
        yes.append([])
        zes.append([])
        for v in np.arange(0, 1.05, 0.05):
            for i in range(0, len(points2)):
                for j in range(0, len(points2[i])):
                    now_x += bernstein(len(points2) - 1, i, u) \
                        * bernstein(len(points2[i]) - 1, j, v) * points2[i][j][0]
                    now_y += bernstein(len(points2) - 1, i, u)\
                        * bernstein(len(points2[i]) - 1, j, v) * points2[i][j][1]
                    now_z += bernstein(len(points2) - 1, i, u) \
                        * bernstein(len(points2[i]) - 1, j, v) * points2[i][j][2]
            xes[-1].append(round(now_x, 2))
            yes[-1].append(round(now_y, 2))
            zes[-1].append(round(now_z, 2))
            now_x = 0
            now_y = 0
            now_z = 0

    xes = np.array(xes)
    yes = np.array(yes)
    zes = np.array(zes)

    axes3d.plot_surface(xes, yes, zes, rstride=1, cstride=1, cmap=color_surface)
    axes3d.plot_wireframe(x1, y1, z1, rstride=1, cstride=1, edgecolor=color_line)
    axes3d.plot_wireframe(x2, y2, z2, rstride=1, cstride=1, edgecolor=color_line2)
    axes1.scatter(x1, y1, 6, color='r')
    axes2.scatter(y1, z1, 6, color='r')
    axes3.scatter(x1, z1, 6, color='r')
    axes1.scatter(x2, y2, 6, color='r')
    axes2.scatter(y2, z2, 6, color='r')
    axes3.scatter(x2, z2, 6, color='r')
    axes1.scatter(xes, yes, 1, color='b')
    axes2.scatter(yes, zes, 1, color='b')
    axes3.scatter(xes, zes, 1, color='b')


def bezier_surface(points, axes3d, axes1, axes2, axes3, color_line, color_surface):
    x = np.array([[q[0] for q in row] for row in points])
    y = np.array([[q[1] for q in row] for row in points])
    z = np.array([[q[2] for q in row] for row in points])

    xes = []
    yes = []
    zes = []
    now_x = 0
    now_y = 0
    now_z = 0

    for u in np.arange(0, 1.05, 0.05):
        xes.append([])
        yes.append([])
        zes.append([])
        for v in np.arange(0, 1.05, 0.05):
            for i in range(0, len(points)):
                for j in range(0, len(points[i])):
                    now_x += bernstein(len(points) - 1, i, u) \
                        * bernstein(len(points[i]) - 1, j, v) * points[i][j][0]
                    now_y += bernstein(len(points) - 1, i, u)\
                        * bernstein(len(points[i]) - 1, j, v) * points[i][j][1]
                    now_z += bernstein(len(points) - 1, i, u) \
                        * bernstein(len(points[i]) - 1, j, v) * points[i][j][2]
            xes[-1].append(round(now_x, 2))
            yes[-1].append(round(now_y, 2))
            zes[-1].append(round(now_z, 2))
            now_x = 0
            now_y = 0
            now_z = 0
    xes = np.array(xes)
    yes = np.array(yes)
    zes = np.array(zes)

    axes3d.plot_surface(xes, yes, zes, rstride=1, cstride=1, cmap=color_surface)
    axes3d.plot_wireframe(x, y, z, rstride=1, cstride=1, edgecolor=color_line)
    axes1.scatter(x, y, 6, color='r')
    axes2.scatter(y, z, 6, color='r')
    axes3.scatter(x, z, 6, color='r')
    axes1.scatter(xes, yes, 1, color='b')
    axes2.scatter(yes, zes, 1, color='b')
    axes3.scatter(xes, zes, 1, color='b')


fig = plt.figure(1)
ax3d = Axes3D(fig, auto_add_to_figure=False)
fig2 = plt.figure(2)
ax1 = fig2.add_subplot(221, aspect='equal')
ax2 = fig2.add_subplot(222, aspect='equal')
ax3 = fig2.add_subplot(223, aspect='equal')
fig.add_axes(ax3d)

control_points = [[[0, 0, 0], [0, 0, 0], [2, 0, 0], [4, 0, 0], [6, 0, 0], [6, 0, 0]],
                  [[0, 0, 0], [0, 0, 0], [2, 0, 1], [4, 0, 1], [6, 0, 0], [6, 0, 0]],
                  [[0, 2, 0], [0, 2, 1], [2, 2, 4], [4, 2, 4], [6, 2, 1], [6, 2, 0]],
                  [[0, 4, 0], [0, 4, 1], [2, 4, 4], [4, 4, 4], [6, 4, 1], [6, 4, 0]],
                  [[0, 6, 0], [0, 6, 0], [2, 6, 1], [4, 6, 1], [6, 6, 0], [6, 6, 0]],
                  [[0, 6, 0], [0, 6, 0], [2, 6, 0], [4, 6, 0], [6, 6, 0], [6, 6, 0]]]
control_points2 = [[[0, 0, 0], [0, 0, 0], [2, 0, 0], [4, 0, 0], [6, 0, 0], [6, 0, 0]],
                   [[0, 0, 0], [0, 0, 0], [2, 0, -1], [4, 0, -1], [6, 0, 0], [6, 0, 0]],
                   [[0, 2, 0], [0, 2, -1], [2, 2, -6], [4, 2, -6], [6, 2, -1], [6, 2, 0]],
                   [[0, 4, 0], [0, 4, -1], [2, 4, -6], [4, 4, -6], [6, 4, - 1], [6, 4, 0]],
                   [[0, 6, 0], [0, 6, 0], [2, 6, -1], [4, 6, -1], [6, 6, 0], [6, 6, 0]],
                   [[0, 6, 0], [0, 6, 0], [2, 6, 0], [4, 6, 0], [6, 6, 0], [6, 6, 0]]]
control_points3 = [[[0, 0, 0], [2, 0, 0], [4, 0, 0], [6, 0, 0]],
                   [[0, 2, 0], [2, 2, 6], [4, 2, -6], [6, 2, 0]],
                   [[0, 4, 0], [2, 4, 6], [4, 4, -6], [6, 4, 0]],
                   [[0, 6, 0], [2, 6, 0], [4, 6, 0], [6, 6, 0]]]
control_points4 = [[[0, 0, 0], [2, 0, 0], [4, 0, 0], [6, 0, 0]],
                   [[0, 2, 0], [2, 2, -6], [4, 2, 6], [6, 2, 0]],
                   [[0, 4, 0], [2, 4, -6], [4, 4, 6], [6, 4, 0]],
                   [[0, 6, 0], [2, 6, 0], [4, 6, 0], [6, 6, 0]]]
control_points5 = [[[0, 0, -2], [1, 0, -2], [2, 0, -2], [4, 0, -2], [5, 0, -2], [6, 0, -2]],
                   [[0, 1, -2], [1, 1, 2], [2, 1, 2], [4, 1, 2], [5, 1, 2], [6, 1, -2]],
                   [[0, 2, -2], [1, 2, 2], [2, 2, -5], [4, 2, -5], [5, 2, 2], [6, 2, -2]],
                   [[0, 4, -2], [1, 4, 2], [2, 4, -5], [4, 4, -5], [5, 4, 2], [6, 4, -2]],
                   [[0, 5, -2], [1, 5, 2], [2, 5, 2], [4, 5, 2], [5, 5, 2], [6, 5, -2]],
                   [[0, 6, -2], [1, 6, -2], [2, 6, -2], [4, 6, -2], [5, 6, -2], [6, 6, -2]]]

control_points6 = [[[0, 0, 1], [1, 0, 2], [2, 0, 3], [3, 0, 3], [4, 0, 2], [5, 0, 1]],
                   [[0, 1, 2], [1, 1, 3], [2, 1, 4], [3, 1, 4], [4, 1, 3], [5, 1, 2]],
                   [[0, 2, 3], [1, 2, 4], [2, 2, 5], [3, 2, 5], [4, 2, 4], [5, 2, 3]],
                   [[0, 3, 3], [1, 3, 4], [2, 3, 5], [3, 3, 5], [4, 3, 4], [5, 3, 3]],
                   [[0, 4, 2], [1, 4, 3], [2, 4, 4], [3, 4, 4], [4, 4, 3], [5, 4, 2]],
                   [[0, 5, 1], [1, 5, 2], [2, 5, 3], [3, 5, 3], [4, 5, 2], [5, 5, 1]]]

# bezier_surface_double(control_points, control_points2, ax3d, ax1, ax2, ax3, 'green', 'red', cm.viridis)
# bezier_surface_double(control_points3, control_points4, ax3d, ax1, ax2, ax3, 'green', 'red', cm.viridis)
# bezier_surface(control_points, ax3d, ax1, ax2, ax3, 'red', cm.viridis)
# bezier_surface(control_points2, ax3d, ax1, ax2, ax3, 'green', cm.inferno)
# bezier_surface(control_points3, ax3d, ax1, ax2, ax3, 'red', cm.viridis)
# bezier_surface(control_points4, ax3d, ax1, ax2, ax3, 'green', cm.inferno)

# bezier_surface(control_points5, ax3d, ax1, ax2, ax3, 'red', cm.viridis)

bezier_surface(control_points6, ax3d, ax1, ax2, ax3, 'red', cm.viridis)

ax3d.set_zlabel("z")
ax3d.set_xlabel("x")
ax3d.set_ylabel("y")
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax2.set_xlabel('y')
ax2.set_ylabel('z')
ax3.set_xlabel('x')
ax3.set_ylabel('z')
ax3d.axes.set_aspect('auto')
plt.show()
