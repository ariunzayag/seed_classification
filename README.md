# Identification of seed coat sculpture 
## Overview 

Seed coat characteristics provide important information in the taxonomy of Allium. The seed coat surface was more diverse. In this work, we explored new classification for Allium seed coats, using CNN network on Scanning Electron Microscopy (SEM) images over 100 species of Allium seeds [(Baasanmunkh et al., 2020)](https://www.mdpi.com/2223-7747/9/9/1239). Seed testa sculpture has divided into two walls: 
1. Anticlinal wall: irregular curved, irregular curved to nearly straight, straight, S, U, UO, O.
2. Periclinal wall: granule, small verrucae, large verrucae, marginal verruca, verrucate verrucae. 

See below for an example of an image.
![image](https://user-images.githubusercontent.com/54767234/189870665-c7356f95-8899-4c4a-ae1a-1c65bde64df5.png)

## Introduction
The project consists of two phases: 
1. Data pre-processing (seed_classification/src/pre-processing/)
2. Classification      (seed_classification/src/supervised/code/)

## Requirements
- tensorflow
- numpy
- scikit-learn
- matplotlib

1. You can clone it and put it you want to put somewhere in your computer
2. Or donwload this repository
3. Run cnn_final_code.py (code is created under seed_classification/src/supervised/code/ folder.

