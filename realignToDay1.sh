cd SubjectData/Subject_$1/Multitasking_Subject$1_Session$2*

if [ $2 = 1 ]; then
cp anat_stripped.nii ..

3dcopy  ProcessedCPCR/clean6+orig cleanDay1_ColorColor_shft_aligned+orig
3dcopy ProcessedWPWR/clean6+orig cleanDay1_WordWord_shft_aligned+orig

3dcopy cleanDay1_ColorColor_shft_aligned+orig ../
3dcopy cleanDay1_WordWord_shft_aligned+orig ../

else
\@Align_Centers -base ../anat_stripped.nii -dset anat_stripped+orig -child ProcessedCPCR/clean6+orig
rm -rf anat_stripped_shft+orig*
\@Align_Centers -base ../anat_stripped.nii -dset anat_stripped+orig -child ProcessedWPWR/clean6+orig

3dvolreg -wtrim -clipit -twopass -zpad 8 -rotcom -verbose -prefix anat_stripped_shft_aligned+orig -base ../anat_stripped.nii -1Dmatrix_save LOC_to_Main anat_stripped_shft+orig

3dAllineate -base ../cleanDay1_ColorColor_shft_aligned+orig -source ProcessedCPCR/clean6_shft+orig. -1Dmatrix_apply LOC_to_Main.aff12.1D -prefix cleanDay$2_ColorColor_shft_aligned+orig -final NN

3dAllineate -base ../cleanDay1_WordWord_shft_aligned+orig -source ProcessedWPWR/clean6_shft+orig. -1Dmatrix_apply LOC_to_Main.aff12.1D -prefix cleanDay$2_WordWord_shft_aligned+orig -final NN

fi
