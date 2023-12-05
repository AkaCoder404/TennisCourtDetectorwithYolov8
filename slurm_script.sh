#!/bin/bash
#SBATCH --job-name=v8_pose
#SBATCH --nodes=4
#SBATCH --gres=gpu:1  # Request one GPU
#SBATCH --cpus-per-task=8  # Number of CPU cores per task
#SBATCH --time=10:00:00  # Request 1 hour of runtime
#SBATCH --mem=16GB  # Request 16GB of RAM
#SBATCH --partition=gpu # Specify the GPU partition
#SBATCH -o ./slurm_outputs/slurm-output-%j.txt  # Write the output to specific directory

# Load required modules (if necessary)
# module load cuda/11.0 cudnn/8.0.4
# module load anaconda3/2020.11

# Activate your Python environment (if using a virtual environment)
# source activate myenv

# Activate your Conda environment (if using a Conda environment)
# conda activate py311

# # Run your PyTorch script
python --version
python train.py

# Jupyter Environment
# jupyter notebook --ip=0.0.0.0 --port=3001 --no-browser
