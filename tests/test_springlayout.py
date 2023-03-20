import pandas as pd
import numpy as np
import netplotbrain
import templateflow.api as tf
import itertools
import pytest

atlas = {'template': 'MNI152NLin2009cAsym',
         'atlas': 'Schaefer2018',
        'desc': '100Parcels7Networks'}
atlasinfo = tf.get(extension='.tsv', **atlas)
atlasinfo = pd.read_csv(atlasinfo, sep='\t')
# Parse the info in to get network names
networks = list(map(lambda x: x.split('_')[2], atlasinfo.name.values))
atlasinfo['yeo7networks'] = networks

# create empty cognitive matrix
edges = np.random.normal(0, 0.025, [100, 100])

# Set within network connectivity to be stronger
for network in atlasinfo['yeo7networks'].unique():
    idx =  atlasinfo[atlasinfo['yeo7networks']==network].index
    idx_pairs = np.array(list(itertools.combinations(idx, 2)))
    edges[idx_pairs[:, 0], idx_pairs[:, 1]] = np.random.normal(0.5, 0.025, [len(idx_pairs)])
    edges[idx_pairs[:, 1], idx_pairs[:, 0]] = np.random.normal(0.5, 0.025, [len(idx_pairs)])

# Rename longer network names
atlasinfo['yeo7networks'].replace('DorsAttn', 'DA', inplace=True)
atlasinfo['yeo7networks'].replace('SalVentAttn', 'VA', inplace=True)

# Resolution argument needed in atlas to get the nii.gz file
atlas['resolution'] = 1
# Plot it all
@pytest.mark.mpl_image_compare
def test_printlayout():
    fig, _ = netplotbrain.plot(template='MNI152NLin2009cAsym',
                    nodes=atlas,
                    nodes_df=atlasinfo,
                    edges=edges,
                    view='LSs', template_style='glass',
                    node_scale=20, node_color='yeo7networks',
                    edge_threshold=0,
                    edge_thresholddirection='>',
                    seed=2022)
    return fig

@pytest.mark.mpl_image_compare
def test_printlayout_legend():
    fig, _ = netplotbrain.plot(template='MNI152NLin2009cAsym',
                    nodes=atlas,
                    nodes_df=atlasinfo,
                    edges=edges,
                    view='LSs', template_style='glass',
                    node_scale=20, node_color='yeo7networks',
                    edge_threshold=0,
                    edge_thresholddirection='>',
                    seed=2022,
                    legend_span=[0, 2])
    return fig
