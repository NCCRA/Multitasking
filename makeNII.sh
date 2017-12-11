cd Subject_$1/Multitasking_Subject$1_Session$2*

module load dcm2niix
cd dcm

for epi in {2..11}
do
mkdir $epi
mv $epi-* $epi/
gunzip $epi/$epi*
dcm2niix $epi
echo "$epi"
done

exit 0

