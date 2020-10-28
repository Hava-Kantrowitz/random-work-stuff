#!/bin/bash
#SBATCH -n 1
#SBATCH --mem 20GB
#SBATCH -t 30:00:00
#SBATCH -o out_maldata
#SBATCH -A netsec
#SBATCH -p standard

module purge
module load anaconda/5.2.0-py3.6 # or anaconda/5.2.0-py2.7
# optional: uncomment next line to use your custom Conda environment; replace 'custom_env' with actual env name
# source activate custom_env

python -u /scratch/hsk4p/http_labels/more_benign.py
