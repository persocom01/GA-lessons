# Author: Joseph Nelson (DC)
'''
Let's say that you're asked to perform hierarchical clustering analysis on a new dataset - how would we go about it?
We're going to be using a dataset that details language skills from different European countries. We will perform a hierarchical clustering analysis on this dataset.
You might be faced with a situation like this is you were asked to tackle demographic info or survey responses, so it's a useful test
'''

from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet
from scipy.spatial.distance import pdist
import numpy as np
import pandas as pd
import os
from scipy.cluster.hierarchy import fcluster, cophenet

%matplotlib inline

# load the data
lang = pd.read_csv()
lang.head()

# scatter to guess clusters
plt.scatter(lang['country'], lang['english'])
plt.show()

# Now, let's convert our data to a matrix to pass to the clustering algorithm - the matrix makes it easier for our algorithm to compute distance:
X = lang.as_matrix(columns=None)

# We'll implement the actual clustering algorithm using the ward method:
Z = linkage(X, 'ward')

# We can calculate the cophenetic correlation coefficient to see how well our algorithm has measured the distances between the points:
c, coph_dists = cophenet(Z, pdist(X))

# let's 'c' how it did
c

# now let's make our dendrogram
plt.title('Dendrogram')
plt.xlabel('Index Numbers')
plt.ylabel('Distance')
dendrogram(
    Z,
    leaf_rotation=90.,
    leaf_font_size=8.,
)
plt.show()


# we can see that no links exist above a distance of 200 - so we will set maximum distance at 200 and use the fclusters function from scipy.cluster.hierarchy, which will return our cluster ID's.
max_dist = 200
clusters = fcluster(Z, max_dist, criterion='distance')
clusters

# Let's plot our data and assign the class labels as the color:
plt.scatter(X[:,0], X[:,6], c=clusters, cmap='prism')
plt.show()
