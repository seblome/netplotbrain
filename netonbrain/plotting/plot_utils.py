import numpy as np
import matplotlib.pyplot as plt

# equal scaling solution from @AndrewCox from https://stackoverflow.com/a/63625222
# Functions from @Mateen Ulhaq and @karlo
def _set_axes_equal(ax: plt.Axes):
    """Set 3D plot axes to equal scale.

    Make axes of 3D plot have equal scale so that spheres appear as
    spheres and cubes as cubes.  Required since `ax.axis('equal')`
    and `ax.set_aspect('equal')` don't work on 3D.
    """
    limits = np.array([
        ax.get_xlim3d(),
        ax.get_ylim3d(),
        ax.get_zlim3d(),
    ])
    origin = np.mean(limits, axis=1)
    radius = 0.5 * np.max(np.abs(limits[:, 1] - limits[:, 0]))
    _set_axes_radius(ax, origin, radius)

def _set_axes_radius(ax, origin, radius):
    x, y, z = origin
    ax.set_xlim3d([x - radius, x + radius])
    ax.set_ylim3d([y - radius, y + radius])
    ax.set_zlim3d([z - radius, z + radius])


def _get_view(views='L', frames=1, arrowaxis='auto'):
    # Order = LRAPDV
    fromview = views[0]
    toview = views[1] if len(views) == 2 else None
    view_defaults = {'L': (180, 10), 'R': (0, 10),
                    'A': (90, 10), 'P': (-90, 10),
                    'D': (-90, 90), 'V': (90, 90)}
    # Set auto arrows for axis depedning on starting view
    if fromview in ['L', 'R']:
        autoarrowaxis = 'AP'
    elif fromview in ['A', 'P']:
        autoarrowaxis = 'LR'
    elif fromview in ['D', 'V']:
        autoarrowaxis = ['LR','AP']
    if toview is None:
        view = view_defaults[fromview]
        vx = [view[0]]
        vy = [view[1]]
    else:
        # Need to add multi direction
        v1x, v1y = view_defaults[fromview]
        v2x, v2y = view_defaults[toview]
        vx = []
        vy = []
        for n in range(frames):
            vx.append(v1x + n * ((v2x - v1x) / (frames - 1)))
            vy.append(v1y + n * ((v2y - v1y) / (frames - 1)))
    if arrowaxis == 'auto':
        arrowaxis = autoarrowaxis

    return vx, vy, arrowaxis