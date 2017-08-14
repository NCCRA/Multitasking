# Multitasking
Public repository for multitasking analyses

fMRI pipeline:
$ generate.nii  <run name> <dcm index> # go from dicoms to nii
do for each run and anatomy, unzips and converts from dicom to nii
makes a folder with name of first parameter.nii

$ 3dSkullStrip -input anat.nii.gz -prefix anat_stripped # everything is better without a skull

$ process_pni2.sh # tshft, align, volreg, mask, scale

$ deconv6_baseline_pni.sh # clean data with trends and motion removed

$ reconSurf.sh <subj id> # FreeSurfer segmentations, atlases, surface volumes (slow)

\@SUMA_Make_Spec_FS -sid <subj id> 

$ makeGreyMatterMask_pni.sh <subj id> # makes gray matter mask, outputs .txt
