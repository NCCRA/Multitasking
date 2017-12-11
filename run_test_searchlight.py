#!/bin/bash

#name job pythondemo, output to slurm file, use partition all, run for 1500 minutes and use 40GB of ram
#SBATCH -J 'testing_abby'
#SBATCH -o logfiles/testing_abby-%j.out
#SBATCH --error=logfiles/testing_abby%j.err
#SBATCH -p all
#SBATCH -t 1
#SBATCH -c 1 --mem 50
#SBATCH --mail-type ALL
#SBATCH --mail-user anovick@princeton.edu
#SBATCH --array=0-24

module load pyger
export PYTHONMALLOC=debug

python -duv /jukebox/cohen/abby/fMRIMultitasking/testSearchlight.py $SLURM_ARRAY_TASK_ID
