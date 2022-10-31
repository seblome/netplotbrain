import numpy as np


def _plot_spheres(ax, nodes, node_columnnames, nodecolor='salmon', nodesize=20, alpha=None, **kwargs):
    """
    Function that plots spheres in figure.

    Parameters
    ---------------
    ax : matplotlib ax
    nodes : dataframe
        node dataframe with x, y, z coordinates.
    node_columnnames : list of string
        name of node column coordinates in datadrame to correspond with x,y,z.
    nodesize : string or float, int
        if string, must refer to a column in nodes.
    nodecolor : string or matplotlib color
        if non-color string, must refer to a column in nodes

    Returns
    -------------
    Nothing

    NOTE: During development, this is not being updated as much as _plot_circles.
    Some functionality from there should be added to this.

    """
    # Get relevant kwargs
    node_scale = kwargs.get('node_scale')
    node_alpha = kwargs.get('node_alpha')
    # Loop through each node and plot a surface plot
    for index, row in nodes.iterrows():
        # Get the xyz coords for the node
        c = [row[node_columnnames[0]],
             row[node_columnnames[1]],
             row[node_columnnames[2]]]

        # Check if nodesize is in the dataframe
        if nodesize in nodes.keys():
            r = row[nodesize] * node_scale
        else:
            r = nodesize * node_scale

        u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:50j]

        # Calculate the x,y,z coordinates of each sphere
        x = r*np.cos(u)*np.sin(v)
        y = r*np.sin(u)*np.sin(v)
        z = r*np.cos(v)

        # Select the node color if string or array
        if isinstance(nodecolor, np.ndarray):
            ncolor = nodecolor[index]
        else:
            ncolor = nodecolor

        ax.plot_surface(c[0]+x, c[1]+y, c[2]+z,
                        color=ncolor,
                        alpha=node_alpha)
