cd SubjectData/Subject_$1/Multitasking_Subject$1_Session$2*
#!/bin/bash

3dDeconvolve -input ProcessedCPCR/pb03.SUBJ.r??.scale+orig.HEAD                   \
	-polort 6 \
	-mask ProcessedCPCR/full_mask.SUBJ+orig \
    -nfirst 0                                              \
    -num_stimts 6                                                   \
    -stim_file 1 ProcessedCPCR/dfile_rall.1D'[0]' -stim_base 1 -stim_label 1 roll  \
    -stim_file 2 ProcessedCPCR/dfile_rall.1D'[1]' -stim_base 2 -stim_label 2 pitch \
    -stim_file 3 ProcessedCPCR/dfile_rall.1D'[2]' -stim_base 3 -stim_label 3 yaw   \
    -stim_file 4 ProcessedCPCR/dfile_rall.1D'[3]' -stim_base 4 -stim_label 4 dS \
    -stim_file 5 ProcessedCPCR/dfile_rall.1D'[4]' -stim_base 5 -stim_label 5 dL \
    -stim_file 6 ProcessedCPCR/dfile_rall.1D'[5]' -stim_base 6 -stim_label 6 dP \
    -errts ProcessedCPCR/clean6 \
    -nobucket 
	

3dDeconvolve -input ProcessedWPWR/pb03.SUBJ.r??.scale+orig.HEAD                   \
        -polort 6 \
        -mask ProcessedWPWR/full_mask.SUBJ+orig \
    -nfirst 0                                              \
    -num_stimts 6                                                   \
    -stim_file 1 ProcessedWPWR/dfile_rall.1D'[0]' -stim_base 1 -stim_label 1 roll  \
    -stim_file 2 ProcessedWPWR/dfile_rall.1D'[1]' -stim_base 2 -stim_label 2 pitch \
    -stim_file 3 ProcessedWPWR/dfile_rall.1D'[2]' -stim_base 3 -stim_label 3 yaw   \
    -stim_file 4 ProcessedWPWR/dfile_rall.1D'[3]' -stim_base 4 -stim_label 4 dS \
    -stim_file 5 ProcessedWPWR/dfile_rall.1D'[4]' -stim_base 5 -stim_label 5 dL \
    -stim_file 6 ProcessedWPWR/dfile_rall.1D'[5]' -stim_base 6 -stim_label 6 dP \
    -errts ProcessedWPWR/clean6 \
    -nobucket
