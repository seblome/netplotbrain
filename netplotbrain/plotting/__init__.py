"""Main plotting functions in package."""
from .plot_edges import _plot_edges, _npedges2dfedges
from .plot_nodes import _scale_nodes, _plot_nodes, _select_single_hemisphere_nodes
from .plot_spheres import _plot_spheres
from .plot_templates import _plot_template, _plot_template_style_filled, \
    _plot_template_style_cloudy, _plot_template_style_surface
from .plot_dimarrows import _add_axis_arrows
from .plot_parcels import _get_nodes_from_nii, _plot_parcels
from .plot_title import _add_subplot_title, _add_title
from .process_input import get_frame_input, _process_edge_input, _process_node_input,\
    _init_figure, _check_axinput, _process_highlightedge_input
from .plot_legend import _add_node_color_legend, _add_node_size_legend, _setup_legend
from .plot_gif import _plot_gif
from .plot_springlayout import _plot_springlayout
from .plot_cm import _plot_connectivitymatrix

__all__ = ['_plot_template', '_plot_template_style_filled',
           '_plot_template_style_cloudy',
           '_scale_nodes', '_plot_nodes', '_plot_spheres',
           '_plot_edges', '_plot_template_style_surface',
           '_add_axis_arrows', '_get_nodes_from_nii', '_plot_parcels',
           '_select_single_hemisphere_nodes', '_npedges2dfedges', '_add_subplot_title', 
           '_setup_legend', '_process_edge_input', '_process_node_input', '_add_node_size_legend',
           '_add_node_color_legend', 'get_frame_input', '_init_figure', '_check_axinput', '_plot_gif',
           '_process_highlightedge_input', '_plot_springlayout', '_add_title', '_plot_connectivitymatrix']
