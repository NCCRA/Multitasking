cd SubjectData/Subject_$1/SUMA

echo pwd

3dcopy Subject_$1_recon_SurfVol+orig ../

3dSurf2Vol -spec Subject_$1_recon_lh.spec -surf_A smoothwm -surf_B pial -sv Subject_$1_recon_SurfVol+orig -grid_parent Subject_$1_recon_SurfVol+orig -map_func mask2 -f_steps 50 -prefix lh_gm
3dSurf2Vol -spec Subject_$1_recon_rh.spec -surf_A smoothwm -surf_B pial -sv Subject_$1_recon_SurfVol+orig -grid_parent Subject_$1_recon_SurfVol+orig -map_func mask2 -f_steps 50 -prefix rh_gm

3dcalc -a lh_gm+orig -b rh_gm+orig -expr 'or(equals(a,1),equals(b,1))' -prefix gm

3dSkullStrip -input Subject_$1_recon_SurfVol+orig -prefix Subject_$1_SurfVol_stripped

\@Align_Centers -cm -base ../anat_stripped+orig -dset Subject_$1_SurfVol_stripped+orig -child gm+orig Subject_$1_recon_SurfVol+orig


3dmerge -1blur_fwhm 4.0 -prefix gm_shft_smooth gm_shft+orig

3dresample -master ../cleanDay1_WordWord_shft_aligned+orig. -prefix Subject$1_Session1_WPWR_gm_shft_smooth_resamp+orig -input gm_shft_smooth+orig

3dresample -master ../cleanDay1_ColorColor_shft_aligned+orig. -prefix Subject$1_Session1_CPCR_gm_shft_smooth_resamp+orig -input gm_shft_smooth+orig

3dmaskdump -mask Subject$1_WPWR_gm_shft_smooth_resamp+orig ../ProcessedWPWR/clean6+orig > Subject$1_Day1_WPWR_graymatter.txt

3dmaskdump -mask Subject$1_CPCR_gm_shft_smooth_resamp+orig ../ProcessedCPCR/clean6+orig > Subejct$1_Day1_CPCR_graymatter.txt



















