# This script computes the pattern similarity between subjects at every voxel in the brain via a Brainiak searchlight.

# We are going to see if it works with a test data set

import numpy as np
import sys
from brainiak.searchlight.searchlight import Searchlight
from scipy import stats
import numpy as np
import nibabel as nib
from matplotlib import pyplot as plt
import scipy.io as sio

x = 10
y = 20
z = 30
t = 16

# we want 16 time points, since we'll have 2 time points per  8 conditions
xdata = np.random.rand(x,y,z,t) # Make a 10 by 20 by 30 by 16 array

xmask = np.ones((x, y, z, 1)) #searchlight wants a mask, we'll give it the whole matrix

#making some fake task labels
labelArray = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8])

#zscore it because I'll want to do this with the real data
xdata = stats.zscore(xdata, axis = 1, ddof = 1)

# we'll use global_outputs_all to keep track of results
global_outputs_all = np.zeros((x,y,z,1))

print("global outputs zeroed")

# hardcoded for supreme clarity
# we want the average pattern of activity for our 8 conditions
# conditions = 4 stimuli * 2 tasks (CP vs CR)

Stimulus1CP = xdata[:, :, :, labelArray == 1]
Stimulus1CPmean = np.mean(Stimulus1CP, axis = 3)
print('Stimulus1CPmean')
print(Stimulus1CPmean.shape)
print('Stimulus1CP test values')
print(Stimulus1CPmean[5, 10, 20])


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

# stack all the conditions on top of each other for later use = A.reshape((-1,A.shape[-1]))
Day1x = np.stack([Stimulus1CPmean, Stimulus1CRmean,Stimulus2CPmean,Stimulus2CRmean, 
                     Stimulus3CPmean, Stimulus3CRmean, Stimulus4CPmean, Stimulus4CRmean], axis=-1)

print('Day1x shape')
print(Day1x.shape)
def color_coeff(A,msk,myrad,bcast_var):
    print('searchlight start')
    
    print(A.shape)
    A = A.reshape((-1,A.shape[-1]))
    print("A reshaped")
    # I think I'm supposed to take the transpose here! check my math...
    corrAB = np.corrcoef(A.T,A.T)[8:,:8]
    print("corrAB made")

    corr_eye = np.zeros([8, 8])
    
    corr1_different_colors = corr_eye
   
    corr2_different_colors = corr_eye
  
    corr3_different_colors = corr_eye
 
    corr4_different_colors = corr_eye
  
    #sorry this is ugly. we are looking for places where the same stimulus (color) has high CP/CR correlation.
    #so for each color we get the same color point/color name correlation, 
    # then we subtract from it the correlation between that color and the other colors.

    corr_1_same_color = corrAB[1, 0]
    corr1_different_colors[[0,1, 0,1,0,1, 0,1,0,1, 0,1], [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]] = 1
    corr1_differentcorrs = corrAB[corr1_different_colors == 1]
    corr1 = corr_1_same_color - np.mean(corr1_differentcorrs)

    corr_2_same_color = corrAB[2, 3]
    corr2_different_colors[[2,3, 2,3,2,3, 2,3,2,3, 2,3], [0, 0, 1, 1, 4, 4, 5, 5, 6, 6, 7, 7]] = 1
    corr2_differentcorrs = corrAB[corr2_different_colors == 1]
    corr2 = corr_2_same_color - np.mean(corr2_differentcorrs)

    corr_3_same_color = corrAB[4, 5]
    corr3_different_colors[[4,5, 4,5,4,5, 4,5,4,5, 4,5], [0, 0, 1, 1, 2, 2, 3, 3, 6, 6, 7, 7]] = 1
    corr3_differentcorrs = corrAB[corr3_different_colors == 1]
    corr3 = corr_3_same_color - np.mean(corr3_differentcorrs)

    corr_4_same_color = corrAB[6, 7]
    corr4_different_colors[[6,7, 6,7,6,7, 6,7,6,7, 6,7], [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]] = 1
    corr4_differentcorrs = corrAB[corr4_different_colors == 1]
    corr4 = corr_4_same_color - np.mean(corr4_differentcorrs)
    
    #we return the amount this area seems to represent each color similarly, regardless if its being pointed to/named.
    z  = np.mean([corr1, corr2, corr3, corr4])
    return z    

#not sure what this does
np.seterr(divide='ignore',invalid='ignore')

# Create and run searchlight
sl = Searchlight(sl_rad=5,max_blk_edge=5)
sl.distribute(Day1x,xmask)
sl.broadcast(None)
print('Running Searchlight...')
global_outputs = sl.run_searchlight(color_coeff)

# if we had more than 1 subjects, we could keep track of everybody's data here. global_outputs_all[:,:,:,1] = global_outputs
global_outputs_all = global_outputs        
print(global_outputs_all[0:5, 0:5, 0:5])

# Plot and save searchlight results
np.save("test_global_outputs_all_brainiak_searchlight", global_outputs_all)

# i am not sure what this averaging is supposed to do, so Im skipping it: global_outputs_avg = np.mean(global_outputs_all,3)
global_outputs_avg = global_outputs
global_outputs = np.array(global_outputs_avg, dtype=np.float)

# not sure what all these nonan things are supposed to do...
global_nonans = global_outputs[np.not_equal(global_outputs,None)]
global_nonans = np.reshape(global_nonans,(x,y,z))
#min1 = np.min(global_nonans[~np.isnan(global_nonans)])
#max1 = np.max(global_nonans[~np.isnan(global_nonans)])
img = nib.Nifti1Image(global_outputs, np.eye(4))
nib.save(img,'test_brainiak_searchlight_results.nii.gz')
#np.save(datadir + 'brainiak_searchlight_results',global_outputs)

print('Searchlight is Complete!')

