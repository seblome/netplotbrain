#  
# # Different node styles
#
# [Open interactive notebook in Binder](https://mybinder.org/v2/gh/wiheto/netplotbrain/main?filepath=docs/gallery/node_styles.ipynb)
#
# There are currently three different node style options to choose from: circles, spheres, parcels.
# You just need to change the specification in the node_type argument.

# Import packages
import netplotbrain
import matplotlib.pyplot as plt

fig  = plt.figure()

# Circles
ax = fig.add_subplot(131, projection='3d')
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                            'desc': '100Parcels7Networks',
                            'resolution': 1},
                  template='MNI152NLin6Asym',
                  template_style='glass',
                  template_glass_maxalpha=0.03,
                  view='S',
                  node_type='circles',
                  node_scale=40,
                  node_alpha=1,
                  arrowaxis=None,
                  subtitles='Circles',
                  fig=fig, ax=ax)

# Spheres
ax = fig.add_subplot(132, projection='3d')
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                            'desc': '100Parcels7Networks',
                            'resolution': 1},
                  template='MNI152NLin6Asym',
                  template_style='glass',
                  template_glass_maxalpha=0.03,
                  view='S',
                  node_type='spheres',
                  node_alpha=1,
                  arrowaxis=None,
                  subtitles='Spheres',
                  fig=fig, ax=ax)

# Parcels
ax = fig.add_subplot(133, projection='3d')
netplotbrain.plot(nodes={'atlas': 'Schaefer2018',
                           'desc': '100Parcels7Networks',
                           'resolution': 1},
                  template='MNI152NLin6Asym',
                  template_style=None,
                  view='S',
                  node_type='parcels',
                  node_alpha=1,
                  node_color='tab20c',
                  arrowaxis=None,
                  subtitles='Parcels',
                  fig=fig, ax=ax)
