cd Subject_$1/Multitasking_Subject$1_Session$2*
cp dcm/2/runtransfer_task.nii.gz anat.nii.gz
3dSkullStrip -input anat.nii.gz -prefix anat_stripped
3dAFNItoNIFTI anat_stripped+orig
afni_proc.py -script AFNIprocess \
    -out_dir ProcessedWPWR \
    -scr_overwrite \
    -dsets WP.nii WR.nii \
    -tcat_remove_first_trs 6 \
    -mask_dilate 0 \
    -copy_anat anat_stripped.nii \
    -anat_has_skull no \
    -volreg_align_e2a \
    -volreg_warp_dxyz 2.0 \
    -blocks tshift align volreg mask scale \
    -execute

afni_proc.py -script AFNIprocess \
    -out_dir ProcessedCPCR \
    -scr_overwrite \
    -dsets CP.nii CR.nii \
    -tcat_remove_first_trs 6 \
    -mask_dilate 0 \
    -copy_anat anat_stripped.nii \
    -anat_has_skull no \
    -volreg_align_e2a \
    -volreg_warp_dxyz 2.0 \
    -blocks tshift align volreg mask scale \
    -execute
