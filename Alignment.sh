# Align each session from the same subject to subject space. Needs AFNI
# $1 = subject ID
# $2 = session to align
# $3 = subject space session

\@Align_Centers -base anatDay$3+orig -dset $1/$2/RawData/anat_skull_strip.nii -child $1/$2/Processed/clean6+orig

3dvolreg -wtrim -clipit -twopass -zpad 8 -rotcom -verbose -prefix $1/$2/anatDay$2_shft_aligned+orig -base ..anatDay$3+orig -1Dmatrix_save LOC_to_Main $1/$2/RawData/anat_skull_strip_shft.nii

3dAllineate -base cleanDay$3+orig -source $1/$2/Processed/clean6_shft+orig. -1Dmatrix_apply LOC_to_Main.aff12.1D -prefix $1/$2/cleanDay$2/_shft_aligned+orig -final NN

3dmaskdump -mask graymatter+orig $1/$2/cleanDay$2_shft_aligned+orig > gmDay$2.txt

