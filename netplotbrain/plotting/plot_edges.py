import numpy as np
import pandas as pd


def _npedges2dfedges(edges, edgethreshold=0):
    """
    A function which transforms numpy array edges into dataframe to be compatible
    with all functionality.

    Parameters
    ---------------------
    edges : numpy array
        n x n array of edges
    edgethreshold : float
        only find edges over a certain threshold
    """
    ind = np.where(edges > edgethreshold)
    weights = edges[ind]
    # Create dataframe
    df = pd.DataFrame(data={'i': ind[0], 'j': ind[1], 'weight': weights})
    return df


def _plot_edges(ax, nodes, edges, edgewidth='auto', edgewidthscale=1, edgecolor='k', edgecol=['i', 'j', 'weight']):
    """
    Plots the edges on the plot

    Parameters
    ----------------------------
    ax : matplotlib ax
    nodes : dataframe
        node dataframe with x, y, z coordinates (at least).
    edges : array or dataframe
        numpy array (adj matrix) or edgelist (df.columns = ['i', 'j', 'weight'])
    edgewidth : 'auto', float, int
        Width of edges. If auto, uses weights from array or dataframes.
    edgewidthscale : float, int
        For display purposes, scale edges by value.
    edgecolor : matplotlib color
        Colour of edges
    edgecol : list (2 or 3 elements). Default: ['i', 'j', 'k']
        list of length 2 or 3.
        The first two, reference the node indicies in nodes.
        The third referencees the weights.
    Returns
    ----------------------
    Nothing
    """
    # if dataframe
    for _, row in edges.iterrows():
        #if row[edgecol[0]] != 0 and row[edgecol[1]] != 0:
        if edgewidth != 'auto':
            ew = edgewidth * edgewidthscale
        else:
            ew = row[edgecol[2]] * edgewidthscale
        if row[edgecol[0]] in nodes.index and row[edgecol[1]] in nodes.index:
            xp = nodes.loc[list((row[edgecol[0]], row[edgecol[1]]))]['x']
            yp = nodes.loc[list((row[edgecol[0]], row[edgecol[1]]))]['y']
            zp = nodes.loc[list((row[edgecol[0]], row[edgecol[1]]))]['z']
            ax.plot(xp, yp, zp, color=edgecolor, linewidth=ew)