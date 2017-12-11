# Multitasking
Public repository for multitasking analyses

fMRI pipeline:

*Preprocess*

$ makeNII.sh  <subject #> <session #> # go from dicoms to nii
do for each run and anatomy, unzips and converts from dicom to nii

$ 3dSkullStrip -input anat.nii.gz -prefix anat_stripped # everything is better without a skull

$ process_pni_WPWRCPCR.sh <subject #> <session #> # 
tshft, align, volreg, mask, scale

$ decon_color_word.sh <subject #> <session #> 
# clean data with trends and motion removed

$ reconSurf.sh <subj id> # FreeSurfer segmentations, atlases, surface volumes (slow)
Requires FreeSurfer, can't run on rondo or spock right now, doing this locally right now

\@SUMA_Make_Spec_FS -sid <subj id> 

$ makeGreyMatter.sh <subj id> # makes gray matter mask, outputs .txt

$ realignToDay1.sh <subject> <session> <session #>

*Analyze*

$ MVPA

$ Brainiak searchlight
testSearchlight.py looks at similarity in a toy dataset composed of random numbers
run_test_searchlight.py submits slurm job to spock's scheduler to run the testSearchlight.py
(currently running into memory issues on spock)

https://pythonhosted.org/brainiak/brainiak.searchlight.html
