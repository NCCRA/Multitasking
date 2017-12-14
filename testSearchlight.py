# Authors: Abigail Novick Hoskin and Jamal Williams
# Thanks to Cameron Ellis and the Brainiak team for all their help! 

# This script computes the pattern similarity between subjects at every voxel in the brain via Brainiak's searchlight functionality.
# We will first generate a "brain" full of randomly generated voxel activation patterns.
# We make a "mask" for this "data", but its really just a matrix that selects our whole toy brain.
# We zscore the data, as we assume you would want to do with real data.
# Then we load the labels for our TRs. In this example, we will have 8 conditions, with 2 instances of each condition (so 16 TRs total).
# We average the voxel activation patterns within each condition, then stack them together to feed to the searchlight.
# The searchlight takes our stacked data, a mask for the data, the radius of your searchlight, and the function you want your searchlight to apply to each voxel.
# Here, our function just returns the correlation between some of the conditions.
# Finally, we save our correlations. Since the toy brain is so small, I also print our results :)

# Required to run: Brainiak! You can open an ipython terminal and run this if you have Brainiak installed.
# Not required to run: any of your own data :)

import numpy as np
import sys
from brainiak.searchlight.searchlight import Searchlight
from scipy import stats
import numpy as np
import nibabel as nib
from matplotlib import pyplot as plt
import scipy.io as sio

# radius of your searchlight
sl_rad = 1
sl_edge = 1

# dimmensions for the toy brain
x = 4
y = 4
z = 4
t = 16

# note, only voxels within this toy brain that are considered "valid" since they sit inside the specified searchlight 
# radius will get assigned a value.

xdata = np.random.rand(x,y,z,t) # make our randomly generated data with t time points 

mask_data  = np.ones((x, y, z)) #searchlight wants a mask, we'll give it the whole matrix

#making some fake task labels
labelArray = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8])

#zscore it because we'll  want to do this with the real data
xdata = stats.zscore(xdata, axis = 1, ddof = 1)

# we'll use global_outputs_all to keep track of results. 
# if you have more than 1 subject, the 4th dimminsion can keep track of n subjects.
global_outputs_all = np.zeros((x,y,z,1))

# hardcoded for supreme clarity
# we want the average pattern of activity for our 8 conditions
# conditions = 4 stimuli * 2 tasks (CP vs CR)

Stimulus1CP = xdata[:, :, :, labelArray == 1]
Stimulus1CPmean = np.mean(Stimulus1CP, axis = 3)

Stimulus1CR = xdata[:, :, :, labelArray == 2]
Stimulus1CRmean = np.mean(Stimulus1CR, axis = 3)

Stimulus2CP = xdata[:, :, :, labelArray == 3]
Stimulus2CPmean = np.mean(Stimulus2CP, axis = 3)

Stimulus2CR = xdata[:, :, :, labelArray == 4]
Stimulus2CRmean = np.mean(Stimulus2CR, axis = 3)

Stimulus3CP = xdata[:, :, :, labelArray == 5]
Stimulus3CPmean = np.mean(Stimulus3CP, axis = 3)

Stimulus3CR = xdata[:, :, :, labelArray == 6]
Stimulus3CRmean = np.mean(Stimulus3CR, axis = 3)

Stimulus4CP = xdata[:, :, :, labelArray == 7]
Stimulus4CPmean = np.mean(Stimulus4CP, axis = 3)

Stimulus4CR = xdata[:, :, :, labelArray == 8]
Stimulus4CRmean = np.mean(Stimulus4CR, axis = 3)

stacked_data = np.stack([Stimulus1CPmean, Stimulus1CRmean,Stimulus2CPmean,Stimulus2CRmean, 
                     Stimulus3CPmean, Stimulus3CRmean, Stimulus4CPmean, Stimulus4CRmean], axis=-1)

def corr_func(A,msk,myrad,bcast_var):
    print('searchlight start')
    
    A = np.array(A)
    A = A.reshape((-1,A.shape[-1]))
    print("A reshaped")
    #m make a correlation matrix
    corrAB = np.corrcoef(A.T,A.T)[8:,:8]
    corr_1_same_color = corrAB[1, 0]
    corr_2_same_color = corrAB[2, 3]
    corr_3_same_color = corrAB[4, 5]
    corr_4_same_color = corrAB[6, 7]
    z = np.mean([corr_1_same_color, corr_2_same_color, corr_3_same_color, corr_4_same_color])
    return z    

np.seterr(divide='ignore',invalid='ignore')

# Create and run searchlight
sl = Searchlight(sl_rad, sl_edge)
sl.distribute([stacked_data],mask_data)
sl.broadcast(None)
print('Running Searchlight...')
global_outputs = sl.run_searchlight(corr_func)

np.save("brainiak_searchlight_tutorial_output", global_outputs_all)

print('Searchlight is Complete!')
print( global_outputs_all)
