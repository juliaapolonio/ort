#!/bin/bash

conda create -n flask-env -y python=3.7
conda install -n ort3d -c conda-forge -y freecad
~/miniconda3/envs/flask-env/bin/pip install -r requirements.txt
wget https://dl.slic3r.org/linux/slic3r-1.3.0-linux-x64.tar.bz2
bzip2 -dc slic3r-1.3.0-linux-x64.tar.bz2 | tar xvf -
rm *.bz2